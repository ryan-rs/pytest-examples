# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
from random import choice


# ======================================================================================================================
# Fixtures
# ======================================================================================================================
# noinspection PyUnusedLocal
@pytest.fixture(scope='class')
def steps_setup_fixture():
    """This fixture demonstrates the isolating a fixture in a setup step."""

    # Setup
    number = choice(range(10))

    yield number

    # Teardown
    number = None


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('747b3284-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('K8S-123')
@pytest.mark.test_case_with_steps
class TestCaseParent(object):
    """Verify that an automation engineer can create tests with steps."""

    def test_step_one(self, steps_setup_fixture):
        """Verify that step one passes."""

        assert type(steps_setup_fixture) is int

    def test_step_two(self, steps_setup_fixture):
        """Verify that step two fails."""

        assert type(steps_setup_fixture) is str

    def test_step_three(self, steps_setup_fixture):
        """Verify that step three is skipped."""

        assert type(steps_setup_fixture) is bool


@pytest.mark.test_case_with_steps
@pytest.mark.test_id('747b219a-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('K8S-123')
class TestCaseChild(TestCaseParent):
    """Verify that an automation engineer can create inheritable tests."""

    def test_step_four(self, steps_setup_fixture):
        """Verify that step four is skipped."""

        assert type(steps_setup_fixture) is float
