import logging

import pytest

from selenium.webdriver.remote.remote_connection import LOGGER

from stere.areas import Area, Areas


LOGGER.setLevel(logging.WARNING)


def test_areas_append_wrong_type():
    """Ensure a TypeError is raised when non-Area objects are appended
    to an Areas."""
    a = Areas()
    with pytest.raises(TypeError) as e:
        a.append('1')

    assert str(e.value) == (
        '1 is not an Area. Only Area objects can be inside Areas.'
    )


def test_areas_append():
    """Ensure Area objects can be appended to an Areas."""
    a = Areas()

    area = Area()
    a.append(area)

    assert 1 == len(a)


def test_areas_remove():
    """Ensure Areas.remove() behaves like list.remove()."""
    a = Areas()

    area = Area()
    a.append(area)
    a.remove(area)

    assert 0 == len(a)


def test_areas_len():
    """Ensure Areas reports length correctly."""
    a = Areas(['1', '2', '3'])
    assert 3 == len(a)


def test_areas_containing_type(test_page):
    """Ensure Areas.containing() returns an Areas object."""
    test_page.navigate()

    found_areas = test_page.repeating_area.areas.containing(
        'link', 'Repeating Link 2',
    )

    assert isinstance(found_areas, Areas)


def test_areas_containing(test_page):
    """Ensure Areas.containing() returns valid results."""
    test_page.navigate()

    found_areas = test_page.repeating_area.areas.containing(
        'link', 'Repeating Link 2',
    )

    assert found_areas[0].text.value == 'Repeating Area 2'


def test_areas_containing_invalid_field_name(test_page):
    test_page.navigate()

    with pytest.raises(AttributeError) as e:
        test_page.repeating_area.areas.containing(
            'lunk', 'Repeating Link 2')

    assert str(e.value) == "'Area' object has no attribute 'lunk'"


def test_areas_contain(test_page):
    """Ensure Areas.contain() returns True when a result is found."""
    test_page.navigate()

    assert test_page.repeating_area.areas.contain("link", "Repeating Link 1")


def test_areas_contain_not_found(test_page):
    """Ensure Areas.contain() returns False when a result is not found."""
    test_page.navigate()

    assert not test_page.repeating_area.areas.contain(
        "link", "Repeating Link 666",
    )
