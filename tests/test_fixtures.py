# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import os
import pytest


# ======================================================================================================================
# Fixtures
# ======================================================================================================================
@pytest.fixture
def prefix():
    """A message prefix."""

    return 'The start of the message.'


@pytest.fixture
def message():
    """The message"""

    return '\nThe message!\n'


@pytest.fixture
def suffix():
    """A message suffix."""

    return 'The end of the message.\n'


@pytest.fixture
def static_message_fixture(tmpdir_factory, prefix, message, suffix):
    """A fixture which provides a static message."""

    filename = tmpdir_factory.mktemp('data').join('static_message.txt').strpath
    file_contents = "{0}{1}{2}".format(prefix, message, suffix)

    with open(filename, 'w') as f:
        f.write(file_contents)

    return filename


@pytest.fixture
def static_message_with_setup_teardown_fixture(tmpdir_factory, prefix, message, suffix):
    """A fixture which provides a static message, but uses a custom setup/teardown."""

    # Setup
    filename = '/tmp/static_message.txt'
    file_contents = "{0}{1}{2}".format(prefix, message, suffix)

    with open(filename, 'w') as f:
        f.write(file_contents)

    # Deliver
    yield filename

    # Teardown
    os.remove(filename)


@pytest.fixture
def dyanmic_message_fixture_factory(tmpdir_factory, prefix, suffix):
    """A fixture which provides a static message."""

    filename = tmpdir_factory.mktemp('data').join('dynamic_message.txt').strpath

    def _factory(message):
        file_contents = "{0}{1}{2}".format(prefix, message, suffix)

        with open(filename, 'w') as f:
            f.write(file_contents)

        return filename

    return _factory


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.test_id('747ba3e0-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('K8S-123')
def test_static_message(static_message_fixture, prefix, message, suffix):
    """Verify that the file contains the correct message."""

    with open(static_message_fixture, 'r') as f:
        assert f.read() == "{0}{1}{2}".format(prefix, message, suffix)


@pytest.mark.test_id('747b9fc6-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('K8S-123')
def test_static_message_with_setup_teardown(static_message_with_setup_teardown_fixture, prefix, message, suffix):
    """Verify that the file contains the correct message."""

    with open(static_message_with_setup_teardown_fixture, 'r') as f:
        assert f.read() == "{0}{1}{2}".format(prefix, message, suffix)


@pytest.mark.test_id('747b9b84-aafb-11e8-bfa2-0025227c8120')
@pytest.mark.jira('K8S-123')
def test_dynamic_message(dyanmic_message_fixture_factory, prefix, suffix):
    """Verify that the file contains the correct message."""

    custom_message = 'Wow! Much Custom!'

    with open(dyanmic_message_fixture_factory(custom_message), 'r') as f:
        assert f.read() == "{0}{1}{2}".format(prefix, custom_message, suffix)
