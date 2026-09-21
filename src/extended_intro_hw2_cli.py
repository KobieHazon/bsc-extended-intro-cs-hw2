"""Command-line interface for selected Homework 2 functions."""

from __future__ import annotations

import argparse

from extended_intro_hw2 import dec, inc, is_rotated, lcs_length_2, power_new, square_digit_chain


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    power_parser = subparsers.add_parser("power")
    power_parser.add_argument("base", type=int)
    power_parser.add_argument("exponent", type=int)

    for command in ("increment", "decrement"):
        binary_parser = subparsers.add_parser(command)
        binary_parser.add_argument("binary")

    chain_parser = subparsers.add_parser("square-chain")
    chain_parser.add_argument("number", type=int)

    for command in ("longest-common-substring", "is-rotation"):
        string_parser = subparsers.add_parser(command)
        string_parser.add_argument("first")
        string_parser.add_argument("second")
    return parser


def cli() -> None:
    arguments = build_parser().parse_args()
    try:
        if arguments.command == "power":
            result = power_new(arguments.base, arguments.exponent)
        elif arguments.command == "increment":
            result = inc(arguments.binary)
        elif arguments.command == "decrement":
            result = dec(arguments.binary)
        elif arguments.command == "square-chain":
            result = square_digit_chain(arguments.number)
        elif arguments.command == "longest-common-substring":
            result = lcs_length_2(arguments.first, arguments.second)
        else:
            result = is_rotated(arguments.first, arguments.second)
        print(result)
    except ValueError as error:
        raise SystemExit(f"error: {error}") from error


if __name__ == "__main__":
    cli()
