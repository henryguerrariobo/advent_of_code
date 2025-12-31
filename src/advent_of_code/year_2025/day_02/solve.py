"""Módulo principal de resolución del problema del día dos."""

from __future__ import annotations

from .gift_shop import sum_invalid_ids_in_range_fast
from .parser import parse_range, read_txt_instructions


def solve_day_two() -> int:
    """
    Lee los rangos.

    Desde el archivo de texto y calcula
    la suma total de los IDs inválidos en todos los rangos.
    """
    ranges = read_txt_instructions("data/raw/gift_shop.txt")
    line = ranges[0]
    range_strings = line.split(",")
    parsed_ranges = [parse_range(r) for r in range_strings]

    total = 0
    for start, end in parsed_ranges:
        total += sum_invalid_ids_in_range_fast(start, end)

    return total
