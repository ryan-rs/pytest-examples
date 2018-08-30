# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('747c3b98-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('ASC-891')
def test_better_assert_message():
    assert 0 is True, 'Zero is not true!'


@pytest.mark.test_id('747c3896-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('ASC-891')
def test_show_traceback():
    # noinspection PyUnresolvedReferences
    pytest.helpers.assert_traceback()


@pytest.mark.test_id('747c3562-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('ASC-891')
def test_hide_traceback():
    # noinspection PyUnresolvedReferences
    pytest.helpers.assert_hide_traceback()
