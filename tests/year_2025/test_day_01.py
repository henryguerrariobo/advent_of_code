from __future__ import annotations

from advent_of_code.year_2025.day_01.dial import Dial
from advent_of_code.year_2025.day_01.parser import parse_instruction


def test_example_from_statement():
    instructions = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    parsed = [parse_instruction(i) for i in instructions]

    dial = Dial(start_position=50)

    for instr in parsed:
        dial.run_dial(instr)

    assert dial.count_zero == 3

    print(dial.count_zero)


def test_dial_part_two_example():
    instructions = [
        ("L", 68),
        ("L", 30),
        ("R", 48),
        ("L", 5),
        ("R", 60),
        ("L", 55),
        ("L", 1),
        ("L", 99),
        ("R", 14),
        ("L", 82),
    ]

    dial = Dial(start_position=50)

    for instr in instructions:
        dial.run_dial_part_two(instr)

    assert dial.count_zero == 6
    print(dial.count_zero)
