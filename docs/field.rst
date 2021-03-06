Fields
------

Field
~~~~~

.. autoclass:: stere.fields.Field()

  .. automethod:: stere.fields.Field.includes()

  .. automethod:: stere.fields.Field.before()

  In this example, Dropdown has been subclassed to hover over the element
  before clicking.

  .. code-block:: python

      from stere.fields import Dropdown

      class CSSDropdown(Dropdown):
          """A Dropdown that's customized to hover over the element before attempting
          a select.
          """
          def before(self):
              self.element.mouse_over()

  .. automethod:: stere.fields.Field.after()

  .. automethod:: stere.fields.Field.value_contains()

  .. automethod:: stere.fields.Field.value_equals()


Root
~~~~

.. autoclass:: stere.fields.Root()


Text
~~~~

.. autoclass:: stere.fields.Text()


Performer method
~~~~~~~~~~~~~~~~

A Field can have a single method be designated as a performer.
This causes the method to be called when the Field is inside an Area and that Area's perform() method is called.

For example, Input's performer is the fill() method, and Button's performer is the click() method. Given the following Area:

.. code-block:: python

    search = Area(
        query=Input('id', 'xsearch'),
        submit=Button('id', 'xsubmit'),
    )

and the following script:

.. code-block:: python

    search.perform()


When `search.perform()` is called, `query.fill()` is called, followed by `submit.click()`.

See the documentation for `Area <https://stere.readthedocs.io/en/latest/area.html>`_ for more details.


Calling the performer method explicitly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The performer method is available as `Field.perform()`.

Using the splinter Button Field as an example, the only difference between
`Button.click()` and `Button.perform()` is that perform will return the object
set in the `Field.returns` attribute.
See `Returning Objects <https://stere.readthedocs.io/en/latest/returning_objects.html>`_ for more details.

Calling the performer method implicitly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a page instance is called directly, the `perform()` method will be executed.

The following code will produce the same results:

.. code-block:: python

    button = Button()
    button.perform()


.. code-block:: python

    button = Button()
    button()


Subclassing Field
~~~~~~~~~~~~~~~~~

Field can be subclassed to suit your own requirements.

If the __init__() method is overwritten, make sure to call super() before your own code.

If your class needs specific behaviour when interacting with Areas, it must use the @stere_performer decorator to specify a performer method.


Assigning the performer method
++++++++++++++++++++++++++++++

When creating a new type of Field, the stere_performer class decorator can be used to assign a performer method.

.. code-block:: python

    from stere.fields.decorators import stere_performer

    @stere_performer('philosophize', consumes_arg=False)
    class DiogenesButton(Field):
        def philosophize(self):
            print("As a matter of self-preservation, a man needs good friends or ardent enemies, for the former instruct him and the latter take him to task.")

The `consumes arg` argument should be used to specify if the method should use an argument provided by Area.perform() or not.
