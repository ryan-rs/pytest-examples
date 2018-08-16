# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
pytest_plugins = ['helpers_namespace']


# ======================================================================================================================
# Hooks
# ======================================================================================================================
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords and 'teardown' not in item.name:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.skip("previous test failed (%s)" % previousfailed.name)


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
