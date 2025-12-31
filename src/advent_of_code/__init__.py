"""Punto de entrada principal para Advent of Code."""

from __future__ import annotations

import logging

from advent_of_code.year_2025.day_01.solve import solve_day_01, solve_day_01_part_two
from advent_of_code.year_2025.day_02.solve import solve_day_two


def config_logging() -> None:
    """Configura el sistema de logging del proyecto."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def run() -> None:
    """Ejecuta la solución de Advent of Code."""
    config_logging()

    logging.info("🎄 Ejecutando Advent of Code 2025")

    result = solve_day_01()
    result_part_two = solve_day_01_part_two()

    logging.info("✅ Resultado Day 01: %s", result)

    logging.info(
        "✅ Resultado  según  el metodo ´0x434C49434B´ es: %s", result_part_two
    )
    result_day_two = solve_day_two()
    logging.info("✅ Resultado Day 02: %s", result_day_two)


if __name__ == "__main__":
    run()
