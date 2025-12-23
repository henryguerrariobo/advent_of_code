"""Solución del día 01 de Advent of Code 2025."""

from __future__ import annotations

from .dial import Dial
from .parser import parse_instruction, read_txt_instructions


def solve_day_01() -> int:
    """
    Ejecuta la solución del día 01.

    Lee las instrucciones, simula el movimiento del dial
    y devuelve cuántas veces el dial termina en la posición 0.

    Returns:
        int: Número de veces que el dial apunta a 0.

    """
    instructions = read_txt_instructions("data/raw/dial.txt")
    parsed = [parse_instruction(i) for i in instructions]

    dial = Dial()
    for instr in parsed:
        dial.run_dial(instr)

    return dial.count_zero
