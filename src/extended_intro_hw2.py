"""Maintained implementations of the Homework 2 programming questions."""

from __future__ import annotations

import random
from collections.abc import Hashable, Sequence

__all__ = [
    "count_ends",
    "count_nums_1",
    "dec",
    "gen_str",
    "has_common",
    "inc",
    "is_rotated",
    "lcs_length_1",
    "lcs_length_2",
    "pow_digit_chain",
    "power_new",
    "reverse_dict",
    "reverse_dict_in_place",
    "square_digit_chain",
]


def reverse_dict(mapping: dict[Hashable, Hashable]) -> dict[Hashable, Hashable]:
    """Return an inverted one-to-one mapping."""
    try:
        reversed_mapping = {value: key for key, value in mapping.items()}
    except TypeError as error:
        raise ValueError("dictionary values must be hashable") from error
    if len(reversed_mapping) != len(mapping):
        raise ValueError("dictionary values must be unique")
    return reversed_mapping


def reverse_dict_in_place(mapping: dict[Hashable, Hashable]) -> None:
    """Invert a one-to-one mapping while preserving its identity."""
    reversed_mapping = reverse_dict(mapping)
    mapping.clear()
    mapping.update(reversed_mapping)


def power_new(base: int | float, exponent: int) -> int | float:
    """Compute a non-negative integer power using exponentiation by squaring."""
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    result: int | float = 1
    factor = base
    remaining = exponent
    while remaining:
        if remaining & 1:
            result *= factor
        factor *= factor
        remaining >>= 1
    return result


def inc(binary: str) -> str:
    """Increment a binary string and return a normalized representation."""
    bits = _binary_bits(binary)
    index = len(bits) - 1
    while index >= 0 and bits[index] == "1":
        bits[index] = "0"
        index -= 1
    if index < 0:
        bits.insert(0, "1")
    else:
        bits[index] = "1"
    return _normalize_binary(bits)


def dec(binary: str) -> str:
    """Decrement a positive binary string and return a normalized representation."""
    bits = _binary_bits(binary)
    if not any(bit == "1" for bit in bits):
        raise ValueError("cannot decrement zero")
    index = len(bits) - 1
    while bits[index] == "0":
        bits[index] = "1"
        index -= 1
    bits[index] = "0"
    return _normalize_binary(bits)


def square_digit_chain(number: int) -> int:
    """Return whether a decimal square-digit chain reaches 1 or 89 first."""
    if number < 1:
        raise ValueError("number must be positive")
    while number not in {1, 89}:
        number = _digit_power_sum(number, 2)
    return number


def count_nums_1(limit: int) -> int:
    """Count positive integers below ``limit`` whose square chain reaches 1."""
    return sum(square_digit_chain(number) == 1 for number in range(1, max(1, limit)))


def pow_digit_chain(number: int, power: int) -> int:
    """Return the first repeated value in a digit-power chain."""
    if number < 1:
        raise ValueError("number must be positive")
    if power < 1:
        raise ValueError("power must be positive")
    seen: set[int] = set()
    while number not in seen:
        seen.add(number)
        number = _digit_power_sum(number, power)
    return number


def count_ends(limit: int, power: int) -> dict[int, int]:
    """Count first-repeat endpoints for digit-power chains below ``limit``."""
    counts: dict[int, int] = {}
    for number in range(1, max(1, limit)):
        endpoint = pow_digit_chain(number, power)
        counts[endpoint] = counts.get(endpoint, 0) + 1
    return counts


def has_common(first: str, second: str, length: int) -> bool:
    """Return whether two strings share a substring of the requested length."""
    if length < 0:
        raise ValueError("length must be non-negative")
    if length == 0:
        return True
    if min(len(first), len(second)) < length:
        return False
    candidates = {first[index : index + length] for index in range(len(first) - length + 1)}
    return any(
        second[index : index + length] in candidates for index in range(len(second) - length + 1)
    )


def lcs_length_1(first: str, second: str) -> int:
    """Find the longest common substring length by repeated membership checks."""
    length = 1
    while has_common(first, second, length):
        length += 1
    return length - 1


def lcs_length_2(first: str, second: str) -> int:
    """Find the longest common substring length with dynamic programming."""
    if len(first) < len(second):
        first, second = second, first
    previous = [0] * (len(second) + 1)
    longest = 0
    for first_character in first:
        current = [0]
        for index, second_character in enumerate(second, start=1):
            value = previous[index - 1] + 1 if first_character == second_character else 0
            current.append(value)
            longest = max(longest, value)
        previous = current
    return longest


def gen_str(length: int, alphabet: Sequence[str], *, rng: random.Random | None = None) -> str:
    """Generate a random string from a non-empty alphabet."""
    if length < 0:
        raise ValueError("length must be non-negative")
    if not alphabet:
        raise ValueError("alphabet must not be empty")
    generator = rng or random
    return "".join(generator.choice(alphabet) for _ in range(length))


def is_rotated(first: str, second: str) -> bool:
    """Return whether two non-empty strings are cyclic rotations of one another."""
    return bool(first) and len(first) == len(second) and first in (second + second)


def _digit_power_sum(number: int, power: int) -> int:
    return sum(int(digit) ** power for digit in str(number))


def _binary_bits(binary: str) -> list[str]:
    if not binary or set(binary) - {"0", "1"}:
        raise ValueError("binary must be a non-empty string containing only 0 and 1")
    return list(binary)


def _normalize_binary(bits: list[str]) -> str:
    return "".join(bits).lstrip("0") or "0"
