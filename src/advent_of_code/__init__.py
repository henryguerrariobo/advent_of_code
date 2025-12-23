"""Punto de entrada principal para Advent of Code."""

from __future__ import annotations

import logging

from advent_of_code.year_2025.day_01.solve import solve_day_01


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

    logging.info("✅ Resultado Day 01: %s", result)


if __name__ == "__main__":
    run()
