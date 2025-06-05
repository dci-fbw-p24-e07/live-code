import pytest

from app import compare_to_seven


def test_eight_is_higher_than_seven():
    assert compare_to_seven(8) == "8 is higher than 7."


def test_string_eight_is_higher_than_seven():
    assert compare_to_seven("8") == "8 is higher than 7."


def test_six_is_lower_than_seven():
    assert compare_to_seven(6) == "6 is lower than 7."


def test_string_six_is_lower_than_seven():
    assert compare_to_seven("6") == "6 is lower than 7."


def test_seven_is_seven():
    assert compare_to_seven(7) == "7 is 7."


def test_string_seven_is_seven():
    assert compare_to_seven("7") == "7 is 7."


def test_string_77_is_higher_than_seven():
    assert compare_to_seven("77") == "77 is higher than 7."


def test_string_f77_is_lower_than_seven():
    assert compare_to_seven("f77") == "f77 is lower than 7."


def test_string_A_is_higher_than_seven():
    assert compare_to_seven("A") == "A is higher than 7."


def test_emptystring_is_lower_than_seven():
    assert compare_to_seven("") == " is lower than 7."


def test_null_character_is_lower_than_seven():
    assert compare_to_seven("\0") == "\0 is lower than 7."


def test_compare_to_seven_is_higher_than_seven():
    assert type(compare_to_seven(compare_to_seven)) == str
