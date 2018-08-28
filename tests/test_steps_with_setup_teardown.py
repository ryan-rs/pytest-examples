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
@pytest.mark.incremental
class TestStepsWithSetupAndTeardown(object):
    @pytest.mark.jira('K8S-123')
    def test_setup_step(self, steps_setup_teardown_fixture):
        steps_setup_teardown_fixture.setup()

    @pytest.mark.jira('K8S-123')
    def test_step_one(self, steps_setup_teardown_fixture):
        assert type(steps_setup_teardown_fixture.number) is int

    @pytest.mark.jira('K8S-123')
    def test_step_two(self, steps_setup_teardown_fixture):
        assert type(steps_setup_teardown_fixture.number) is str

    @pytest.mark.jira('K8S-123')
    def test_step_three(self, steps_setup_teardown_fixture):
        assert type(steps_setup_teardown_fixture.number) is bool

    @pytest.mark.jira('K8S-123')
    def test_teardown_step(self, steps_setup_teardown_fixture):
        steps_setup_teardown_fixture.teardown()
