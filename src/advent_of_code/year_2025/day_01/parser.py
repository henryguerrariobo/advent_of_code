"""Módulo encargado de leer y procesar las instrucciones del dial."""

from __future__ import annotations

from pathlib import Path

__all__ = ["read_txt_instructions", "parse_instruction"]


def read_txt_instructions(path: str) -> list[str]:
    """
    Lee el archivo de instrucciones del dial.

    Args:
        path (str): Ruta del archivo de texto.

    Returns:
        list[str]: Lista de instrucciones sin líneas vacías.

    """
    with Path(path).open() as file:
        return [line.strip() for line in file if line.strip()]


def parse_instruction(instr: str) -> tuple[str, int]:
    """
    Convierte una instrucción en una tupla procesable.

    Ejemplo:
        "L68" -> ("L", 68)

    Args:
        instr (str): Instrucción cruda del archivo.

    Returns:
        tuple[str, int]: Dirección y cantidad de pasos.

    """
    return instr[0], int(instr[1:])
