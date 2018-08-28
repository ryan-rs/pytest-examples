# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest


# ======================================================================================================================
# Globals
# ======================================================================================================================
NUMBER = 123


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.skip(reason='Test is flaky.')
@pytest.mark.jira('K8S-123')
@pytest.mark.test_id('747b5458-aafb-11e8-bfa2-0025227c8120')
def test_skip():
    """Verify that a test can be skipped."""

    assert True is False


@pytest.mark.skipif(NUMBER > 0, reason='The NUMBER is too big!')
@pytest.mark.jira('K8S-123')
@pytest.mark.test_id('747b5142-aafb-11e8-bfa2-0025227c8120')
def test_skip_conditionally():
    """Verify that a test can be skipped."""

    assert not NUMBER


@pytest.mark.xfail(strict=True, reason='The NUMBER is too big!')
@pytest.mark.jira('K8S-123')
@pytest.mark.test_id('747b4e0e-aafb-11e8-bfa2-0025227c8120')
def test_expect_fail():
    """Verify that a test can be skipped.

    You can change the default value of the strict parameter using the xfail_strict ini option:

    [pytest]
    xfail_strict=true
    """

    assert NUMBER
