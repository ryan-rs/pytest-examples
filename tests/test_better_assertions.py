# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('bd53a460-a22b-11e8-9a7b-0025227c8120')
@pytest.mark.jira('K8S-123')
def test_show_traceback():
    # noinspection PyUnresolvedReferences
    pytest.helpers.assert_traceback()


@pytest.mark.test_id('28c60480-a22d-11e8-8bd3-0025227c8120')
@pytest.mark.jira('K8S-123')
def test_hide_traceback():
    # noinspection PyUnresolvedReferences
    pytest.helpers.assert_hide_traceback()
