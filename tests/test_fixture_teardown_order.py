# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest


# ======================================================================================================================
# Fixtures
# ======================================================================================================================
@pytest.fixture
def fixture_a():
    """A message prefix."""

    print('\nfixture_a setup')
    yield
    print('\nfixture_a teardown')


@pytest.fixture
def fixture_b():
    """A message prefix."""

    print('\nfixture_b setup')
    yield
    print('\nfixture_b teardown')


@pytest.fixture
def fixture_c(fixture_a, fixture_b):
    """A message prefix."""

    print('\nfixture_c setup')
    yield
    print('\nfixture_c teardown')


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('748ba3e0-aafb-11e8-bfa2-0025227d8120')
@pytest.mark.jira('ASC-891')
def test_tear_it_down(fixture_c):
    """Verify that the file contains the correct message."""

    print('\nTest!')
