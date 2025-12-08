"""En este módulo se descargan los datos de la fuente de datos."""

from __future__ import annotations

import logging

from advent_of_code.config import ProjectConfig


def analyze_data(execute_module: bool, config: ProjectConfig) -> None:
    """Analizando los datos."""
    if not execute_module:
        logging.info("⏭️ Módulo ANALYZE deshabilitado, omitiendo análisis de datos")
        return

    print("Analizando los datos", config)

    return
