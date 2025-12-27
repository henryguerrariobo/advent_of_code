"""Inicialización del paquete del día 01."""

from __future__ import annotations

from .dial import Dial
from .parser import parse_instruction, read_txt_instructions
from .solve import solve_day_01, solve_day_01_part_two

__all__ = [
    "Dial",
    "parse_instruction",
    "read_txt_instructions",
    "solve_day_01",
    "solve_day_01_part_two",
]
