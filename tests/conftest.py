# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
pytest_plugins = ['helpers_namespace']


# ======================================================================================================================
# Helpers
# ======================================================================================================================
# noinspection PyUnresolvedReferences
@pytest.helpers.register
def assert_traceback():
    """This assert helper demonstrates how to hide extraneous assertion output for more readable failure summaries."""

    assert False


# noinspection PyUnresolvedReferences
@pytest.helpers.register
def assert_hide_traceback():
    """This assert helper demonstrates how to hide extraneous assertion output for more readable failure summaries."""

    __tracebackhide__ = True

    assert False


# noinspection PyUnresolvedReferences
@pytest.helpers.register
def merge_dicts(*args):
    """Given any number of dicts, shallow copy and merge into a new dict, precedence goes to key value pairs in latter
    dicts.

    Args:
        *args (list(dict)): A list of dictionaries to be merged.

    Returns:
        dict: A merged dictionary.
    """

    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result


# noinspection PyUnresolvedReferences
@pytest.helpers.register
def is_sub_dict(small, big):
    """Determine if one dictionary is a subset of another dictionary.

    Args:
        small (dict): A dictionary that is proposed to be a subset of another dictionary.
        big (dict): A dictionary that is a superset of another dictionary.

    Returns:
        bool: A bool indicating if the small dictionary is in fact a sub-dictionary of big
    """

    return dict(big, **small) == big
