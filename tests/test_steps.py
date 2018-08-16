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
# noinspection PyUnusedLocal
@pytest.fixture(scope='class')
def steps_setup_fixture():
    """This fixture demonstrates the isolating a fixture in a setup step."""

    # Setup
    number = choice(range(10))

    yield number

    # Teardown
    number = None


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
class TestStepsWithOnlySetup(object):
    @pytest.mark.test_id('4daaec56-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_setup_step(self, steps_setup_fixture):
        assert type(steps_setup_fixture) is int

    @pytest.mark.test_id('4daae936-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_step_one(self, steps_setup_fixture):
        assert type(steps_setup_fixture) is int

    @pytest.mark.test_id('4daae5ee-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_step_two(self, steps_setup_fixture):
        assert type(steps_setup_fixture) is str

    @pytest.mark.test_id('4daade64-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_step_three(self, steps_setup_fixture):
        assert type(steps_setup_fixture) is bool


@pytest.mark.incremental
class TestStepsWithSetupAndTeardown(object):
    @pytest.mark.test_id('4daadb62-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_setup_step(self, steps_setup_teardown_fixture):
        steps_setup_teardown_fixture.setup()

    @pytest.mark.test_id('4daad860-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_step_one(self, steps_setup_teardown_fixture):
        assert type(steps_setup_teardown_fixture.number) is int

    @pytest.mark.test_id('4daad54a-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_step_two(self, steps_setup_teardown_fixture):
        assert type(steps_setup_teardown_fixture.number) is str

    @pytest.mark.test_id('4daad22a-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_step_three(self, steps_setup_teardown_fixture):
        assert type(steps_setup_teardown_fixture.number) is bool

    @pytest.mark.test_id('4daac7d0-a1a7-11e8-a371-0025227c8120')
    @pytest.mark.jira('K8S-123')
    def test_teardown_step(self, steps_setup_teardown_fixture):
        steps_setup_teardown_fixture.teardown()


@pytest.mark.incremental
class TestStepsWithSetupAndTeardownMore(TestStepsWithSetupAndTeardown):
    @pytest.mark.test_id('4daadb62-a1a7-11e8-a371-0025247c8120')
    @pytest.mark.jira('K8S-123')
    def test_new_step(self, steps_setup_teardown_fixture):
        steps_setup_teardown_fixture.setup()
