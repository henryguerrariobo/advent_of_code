"""Módulo de lectura y parseo de instrucciones desde archivos de texto."""

from __future__ import annotations

from pathlib import Path

__all__ = ["read_txt_instructions", "parse_range"]


def read_txt_instructions(path: str) -> list[str]:
    """
    Lee un archivo de texto y devuelve una lista de líneas no vacías.

    Cada línea se limpia de espacios y saltos de línea.
    """
    with Path(path).open() as file:
        return [line.strip() for line in file if line.strip()]


def parse_range(range_str: str) -> tuple[int, int]:
    """
    Recibe un rango en formato "A-B" y lo separa en dos números.

    Ejemplo:
        "10-25" → (10, 25)
    """
    start, end = range_str.split("-")
    return int(start), int(end)
