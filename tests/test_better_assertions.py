# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest


# ======================================================================================================================
# Test Cases
# ======================================================================================================================

@pytest.mark.jira('K8S-123')
def test_better_assert_message():
    assert 0 is True, 'Zero is not true!'


@pytest.mark.jira('K8S-123')
def test_show_traceback():
    # noinspection PyUnresolvedReferences
    pytest.helpers.assert_traceback()



@pytest.mark.jira('K8S-123')
def test_hide_traceback():
    # noinspection PyUnresolvedReferences
    pytest.helpers.assert_hide_traceback()
