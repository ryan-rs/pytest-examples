# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
import string
from random import choice


# ======================================================================================================================
# Code Under Test
# ======================================================================================================================
def inc(number):
    """Increment a integer by one."""

    return number + 1


def hide_the_word(word):
    """Wrap a provided word in a string of random characters."""

    return "{0}{word}{0}".format(''.join(choice(string.ascii_letters) for _ in range(choice(range(20)))), word=word)


def generate_words(words):
    """Create a list of words with appended integers from a list of provided words"""

    return ["{}{}".format(word, number) for word, number in zip(words, range(len(words)))]


def raise_exception(number):
    """Raise an exception when a user provides integer above 1."""

    if number > 1:
        raise RuntimeError("Number is above one! Number: {}".format(number))


# ======================================================================================================================
# Test Cases
# ======================================================================================================================
@pytest.mark.jira('K8S-123')
def test_inc():
    """Verify that 'inc' actually works!"""

    assert inc(3) == 4


@pytest.mark.jira('K8S-123')
def test_hide_the_word():
    """Verify that the hidden word is inside the string."""

    word = 'hidden'

    assert word in hide_the_word(word)


@pytest.mark.jira('K8S-123')
def test_existence():
    """Verify that the hidden word is inside the string."""

    empty_string = ''
    empty_list = []
    empty_dict = {}
    none_object = None

    assert not empty_string
    assert not empty_list
    assert not empty_dict
    assert not none_object

    assert len(empty_string) == 0
    assert len(empty_list) == 0
    assert len(empty_dict) == 0
    assert none_object is None


@pytest.mark.jira('K8S-123')
def test_zipping():
    """Verify a function that appends an integer at the end of a word."""

    words = ['special', 'words', 'are', 'cool']

    for new_word, number in zip(generate_words(words), range(len(words))):
        assert new_word == "{}{}".format(words[number], number)


@pytest.mark.jira('K8S-123')
def test_expect_exception():
    """Verify a function raises a specific exception when provided bad input."""

    number = 3

    with pytest.raises(RuntimeError) as exception:
        raise_exception(number)

    assert exception.value.message == 'Number is above one! Number: 3'
