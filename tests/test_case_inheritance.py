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
@pytest.mark.test_case_with_steps
class TestCaseParent(object):
    """Verify that an automation engineer can create tests with steps."""

    @pytest.mark.jira('K8S-123')
    def test_step_one(self, steps_setup_fixture):
        """Verify that step one passes."""

        assert type(steps_setup_fixture) is int

    @pytest.mark.jira('K8S-123')
    def test_step_two(self, steps_setup_fixture):
        """Verify that step two fails."""

        assert type(steps_setup_fixture) is str

    @pytest.mark.jira('K8S-123')
    def test_step_three(self, steps_setup_fixture):
        """Verify that step three is skipped."""

        assert type(steps_setup_fixture) is bool


@pytest.mark.test_case_with_steps
class TestCaseChild(TestCaseParent):
    @pytest.mark.jira('K8S-123')
    def test_step_four(self, steps_setup_fixture):
        """Verify that step four is skipped."""

        assert type(steps_setup_fixture) is float
