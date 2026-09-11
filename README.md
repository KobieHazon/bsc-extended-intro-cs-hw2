# Extended Introduction to Computer Science - Homework 2

A 2017 CS BSc Python assignment covering dictionary inversion, exponentiation by squaring, binary-string arithmetic, digit-power chains, longest common substrings, and cyclic string rotations.

## Exercises

- Reverse one-to-one dictionaries, including an in-place variant that preserves object identity.
- Compute integer powers using the binary representation of the exponent.
- Increment and decrement binary strings without converting them to integers.
- Analyze square-digit and generalized digit-power chains.
- Compare direct substring search with a dynamic-programming longest-common-substring algorithm.
- Detect cyclic string rotations.

## Setup

```bash
git clone https://github.com/KobieHazon/bsc-extended-intro-cs-hw2.git
cd bsc-extended-intro-cs-hw2
uv sync --dev
```

The maintained package supports Python 3.10 or newer and has no runtime dependencies.

## Usage

```bash
uv run extended-intro-hw2 power 2 10
uv run extended-intro-hw2 increment 111
uv run extended-intro-hw2 square-chain 85
uv run extended-intro-hw2 longest-common-substring abcaabcd dbcaaabc
uv run extended-intro-hw2 is-rotation amirrub rubamir
```

The commands print `1024`, `1000`, `89`, `4`, and `True`, respectively.

## Testing

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The regression suite covers every maintained function, invalid input behavior, command-line output, and the complete supplied tester. The untouched recovered solution passes all supplied checks except one known case: it returns `False` when both non-empty strings are identical, although the tester expects identical strings to count as rotations. The maintained implementation corrects that case and passes the full tester.

## Repository Structure

- `assignment/hw2_tester.py`: supplied tester preserved in its original form
- `assignment/score-key.pdf`: supplied grading key
- `solution/written-answers.pdf`: my six-page written submission
- `src/extended_intro_hw2/`: maintained implementations and command-line interface
- `tests/`: portable pytest suite, including a compatibility run of the supplied tester

## Implementation notes

The recovered Python file combines my answers with course-provided skeleton comments and named benchmark snippets. Those supplied sections remain in the historical solution commit and are not presented as authored work.

## License

No repository-wide license is declared because the repository combines original work with supplied material whose reuse terms were not recorded.
