import pytest

from app import squared


def test_squared_of_1_is_1():
    assert squared(1) == 1


def test_squared_of_10_is_100():
    assert squared(10) == 100


def test_squared_of_negative_two_is_not_negative_four():
    assert squared(-2) != -4


def test_squared_is_a_function():
    assert callable(squared)


def test_squared_of_20_returns_integer():
    assert type(squared(20)) is int


def test_squared_of_string_raises_type_error():
    with pytest.raises(TypeError):
        squared("fish")
