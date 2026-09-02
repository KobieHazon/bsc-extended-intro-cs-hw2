import random

import pytest

from extended_intro_hw2 import (
    count_ends,
    count_nums_1,
    dec,
    gen_str,
    has_common,
    inc,
    is_rotated,
    lcs_length_1,
    lcs_length_2,
    pow_digit_chain,
    power_new,
    reverse_dict,
    reverse_dict_in_place,
    square_digit_chain,
)


def test_dictionary_reversal_preserves_input() -> None:
    original = {18: "rabbits", 3: "cats", 12: 234}

    assert reverse_dict(original) == {"rabbits": 18, "cats": 3, 234: 12}
    assert original == {18: "rabbits", 3: "cats", 12: 234}


def test_dictionary_reversal_in_place_preserves_identity() -> None:
    original = {23: "dogs", 36: "cats", 198: 234}
    identity = id(original)

    assert reverse_dict_in_place(original) is None
    assert id(original) == identity
    assert original == {"dogs": 23, "cats": 36, 234: 198}


@pytest.mark.parametrize("mapping", [{1: "same", 2: "same"}, {1: []}])
def test_dictionary_reversal_rejects_invalid_values(mapping) -> None:
    with pytest.raises(ValueError):
        reverse_dict(mapping)


@pytest.mark.parametrize(
    ("base", "exponent"),
    [(27, 10), (42, 77), (15, 0), (-3, 5), (2, 200)],
)
def test_power_new_matches_builtin_power(base: int, exponent: int) -> None:
    assert power_new(base, exponent) == base**exponent


def test_power_new_rejects_negative_exponent() -> None:
    with pytest.raises(ValueError):
        power_new(2, -1)


@pytest.mark.parametrize(
    ("binary", "expected"),
    [("0", "1"), ("1", "10"), ("101", "110"), ("111", "1000"), ("001", "10")],
)
def test_increment(binary: str, expected: str) -> None:
    assert inc(binary) == expected


@pytest.mark.parametrize(
    ("binary", "expected"),
    [("1", "0"), ("101", "100"), ("100", "11"), ("11", "10"), ("0010", "1")],
)
def test_decrement(binary: str, expected: str) -> None:
    assert dec(binary) == expected


@pytest.mark.parametrize("binary", ["", "102", "-1", "abc"])
def test_binary_operations_reject_invalid_strings(binary: str) -> None:
    with pytest.raises(ValueError):
        inc(binary)


def test_decrement_rejects_zero() -> None:
    with pytest.raises(ValueError):
        dec("000")


@pytest.mark.parametrize(("number", "expected"), [(44, 1), (50, 89), (85, 89), (135, 89)])
def test_square_digit_chain(number: int, expected: int) -> None:
    assert square_digit_chain(number) == expected


def test_square_chain_counts_match_supplied_cases() -> None:
    assert count_nums_1(1) == 0
    assert count_nums_1(50) == 11
    assert count_nums_1(100) == 19


@pytest.mark.parametrize(
    ("number", "power", "expected"), [(70, 1, 7), (61, 4, 13139), (50, 7, 5221343), (1, 1, 1)]
)
def test_digit_power_chain(number: int, power: int, expected: int) -> None:
    assert pow_digit_chain(number, power) == expected


def test_digit_power_chain_endpoint_counts_match_supplied_cases() -> None:
    assert count_ends(33, 3) == {1: 2, 370: 2, 371: 11, 133: 5, 217: 2, 153: 10}
    assert count_ends(80, 4) == {8208: 6, 1: 2, 4338: 2, 4179: 1, 13139: 67, 6514: 1}


@pytest.mark.parametrize(
    ("first", "second", "length", "expected"),
    [
        ("abcaabcd", "dbcaaabc", 5, False),
        ("abcaabcd", "dbcaaabc", 4, True),
        ("", "dbcaaabc", 4, False),
        ("anything", "else", 0, True),
    ],
)
def test_common_substrings(first: str, second: str, length: int, expected: bool) -> None:
    assert has_common(first, second, length) is expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [("abcaabcd", "dbcaaabc", 4), ("asdfreg", "cvbnjt", 0), ("", "abcadbcd", 0)],
)
def test_longest_common_substring_implementations(first: str, second: str, expected: int) -> None:
    assert lcs_length_1(first, second) == expected
    assert lcs_length_2(first, second) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        ("amirrub", "rubamir", True),
        ("omeruri", "omeruri", True),
        ("abc", "cab", True),
        ("abc", "acb", False),
        ("", "", False),
        ("", "abc", False),
    ],
)
def test_rotation(first: str, second: str, expected: bool) -> None:
    assert is_rotated(first, second) is expected


def test_random_string_generation_is_reproducible() -> None:
    assert gen_str(8, "abc", rng=random.Random(7)) == "babcaaca"
