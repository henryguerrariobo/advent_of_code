"""Módulo de validación y cálculo de IDs inválidos."""

from __future__ import annotations

__all__ = ["is_invalid_id", "sum_invalid_ids_in_range_fast"]


def is_invalid_id(number: int) -> bool:
    """
    Determina si un ID es inválido.

    Un ID es inválido si:
    - Tiene una cantidad par de dígitos
    - La primera mitad de los dígitos es igual a la segunda mitad
    """
    id_products = str(number)

    if len(id_products) % 2 != 0:
        return False

    half = len(id_products) // 2
    return id_products[:half] == id_products[half:]


def sum_invalid_ids_in_range_fast(start: int, end: int) -> int:
    """Suma los IDs inválidos dentro de un rango SIN recorrer cada número."""
    total = 0

    len_start = len(str(start))
    len_end = len(str(end))

    for total_len in range(len_start, len_end + 1):
        if total_len % 2 != 0:
            continue  # solo longitudes pares

        half_len = total_len // 2

        min_half = 10 ** (half_len - 1)
        max_half = 10**half_len

        for half in range(min_half, max_half):
            invalid_id = int(str(half) * 2)

            if start <= invalid_id <= end:
                total += invalid_id

    return total
