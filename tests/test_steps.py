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
@pytest.mark.test_id('747c180c-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('ASC-891')
@pytest.mark.test_case_with_steps()
class TestSteps(object):
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


@pytest.mark.test_id('747c0b96-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('ASC-891')
@pytest.mark.test_case_with_steps()
class TestStepsWithOnlySetup(object):
    """Verify that an automation engineer can create tests with steps and explicit setup."""

    def test_setup_step(self, steps_setup_fixture):
        """Verify that setup passes."""

        assert type(steps_setup_fixture) is int

    def test_step_one(self, steps_setup_fixture):
        """Verify that step one passes."""

        assert type(steps_setup_fixture) is int

    def test_step_two(self, steps_setup_fixture):
        """Verify that step two fails."""

        assert type(steps_setup_fixture) is str

    def test_step_three(self, steps_setup_fixture):
        """Verify that step three is skipped."""

        assert type(steps_setup_fixture) is bool
