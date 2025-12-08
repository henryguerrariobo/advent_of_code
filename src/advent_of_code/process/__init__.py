"""En este módulo se descargan los datos de la fuente de datos."""

from __future__ import annotations

import logging

from advent_of_code.config import ProjectConfig


def process_data(execute_module: bool, config: ProjectConfig) -> None:
    """Procesando los datos de la fuente de datos."""
    if not execute_module:
        logging.info("⏭️ Módulo PROCESS deshabilitado, omitiendo procesamiento de datos")
        return

    print("Procesando los datos", config)

    return
