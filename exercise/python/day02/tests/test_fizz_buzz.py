import unittest

from assertpy import assert_that
import pytest

from games.fizz_buzz import FizzBuzz
from tests.ValidInput import ValidInput


@pytest.mark.parametrize(
    "valid_input",
        [
            ValidInput(1, "1"),
            ValidInput(67, "67"),
            ValidInput(82, "82"),
            ValidInput(3, "Fizz"),
            ValidInput(66, "FizzBang"),
            ValidInput(99, "FizzBang"),
            ValidInput(5, "Buzz"),
            ValidInput(50, "Buzz"),
            ValidInput(85, "Buzz"),
            ValidInput(15, "FizzBuzz"),
            ValidInput(30, "FizzBuzz"),
            ValidInput(45, "FizzBuzz"),
        ]
)
def test_returns_its_numbers_representation(valid_input):
    assert FizzBuzz.convert(valid_input.input) == valid_input.expected_result


@pytest.mark.parametrize("out_of_range_input", [0, -1, 101])
def test_fails_for_numbers_out_of_range(out_of_range_input):
    assert FizzBuzz.convert(out_of_range_input) is None


if __name__ == "__main__":
    unittest.main()
