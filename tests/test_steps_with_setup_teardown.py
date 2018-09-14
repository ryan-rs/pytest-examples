# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
from random import choice


# ======================================================================================================================
# Classes
# ======================================================================================================================
class SetupTeardownFixture(object):
    def __init__(self):
        self._number = None

    @property
    def number(self):
        return self._number

    def setup(self):
        self._number = choice(range(10))

    def teardown(self):
        self._number = None


# ======================================================================================================================
# Fixtures
# ======================================================================================================================
@pytest.fixture(scope='session')
def steps_setup_teardown_fixture():
    """This fixture demonstrates using a fixture for a setup and teardown step."""

    fixture = SetupTeardownFixture()

    yield fixture

    # Teardown (Safety mechanism)
    fixture.teardown()


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('747b7b22-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('ASC-891')
@pytest.mark.test_case_with_steps()
class TestStepsWithSetupAndTeardown(object):
    """Verify that an automation engineer can create tests with steps and explicit setup/teardown."""

    def test_setup_step(self, steps_setup_teardown_fixture):
        """Verify that setup passes."""

        steps_setup_teardown_fixture.setup()

    def test_step_one(self, steps_setup_teardown_fixture):
        """Verify that step one passes."""

        assert type(steps_setup_teardown_fixture.number) is int

    def test_step_two(self, steps_setup_teardown_fixture):
        """Verify that step two fails."""

        assert type(steps_setup_teardown_fixture.number) is str

    def test_step_three(self, steps_setup_teardown_fixture):
        """Verify that step three is skipped."""

        assert type(steps_setup_teardown_fixture.number) is bool

    def test_teardown_step(self, steps_setup_teardown_fixture):
        """Verify that teardown runs passes even though previous step is skipped."""

        steps_setup_teardown_fixture.teardown()
