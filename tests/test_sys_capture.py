# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import sys
import pytest
import subprocess


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('fa8ce76a-e696-11e8-8432-0025227c8120')
@pytest.mark.jira('ASC-860')
def test_ignore_capture():
    """Verify that messages printed to 'stdout' and 'stderr' are NOT captured by pytest-zigzag when a test passes."""

    sys.stdout.write('Print to stdout')
    sys.stderr.write('Print to stderr')

    assert True


@pytest.mark.test_id('fa8cd6ee-e696-11e8-8432-0025227c8120')
@pytest.mark.jira('ASC-860')
def test_capture_stdout():
    """Verify that messages printed to 'stdout' are captured by pytest-zigzag upon failure."""

    sys.stdout.write('Print to stdout')

    assert False


@pytest.mark.test_id('ca81e478-e699-11e8-b952-0025227c8120')
@pytest.mark.jira('ASC-860')
def test_capture_stderr():
    """Verify that messages printed to 'stderr' are captured by pytest-zigzag upon failure."""

    sys.stderr.write('Print to stderr')

    assert False


@pytest.mark.test_id('ca81d3fc-e699-11e8-b952-0025227c8120')
@pytest.mark.jira('ASC-860')
def test_capture_both():
    """Verify that messages printed to 'stderr' and 'stdout' are captured by pytest-zigzag upon failure."""

    sys.stdout.write('Print to stdout')
    sys.stderr.write('Print to stderr')

    assert False


@pytest.mark.test_id('897f51d0-e6ae-11e8-9063-0025227c8120')
@pytest.mark.jira('ASC-860')
def test_capture_shell_output():
    """Verify that messages printed to 'stdout' from subprocess are captured upon failure."""

    subprocess.call('ls')

    assert False
