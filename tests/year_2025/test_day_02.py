"""Test para el dia dos y validación de datos."""

from __future__ import annotations

from advent_of_code.year_2025.day_02 import solve_day_two


def test_solve_day_two():
    """
    Verifica que el resultado final del día 2
    sea el esperado para el archivo de entrada real.
    """
    result = solve_day_two()
    assert result == 30608905813
