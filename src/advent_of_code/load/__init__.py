"""En este módulo se descargan los datos de la fuente de datos."""

from __future__ import annotations

import logging

from advent_of_code.config import ProjectConfig


def load_data(execute_module: bool, config: ProjectConfig) -> None:
    """Descarga los datos de la fuente de datos."""
    if not execute_module:
        logging.info("⏭️ Módulo LOAD deshabilitado, omitiendo descarga de datos")
        return

    print("Descargando datos", config)

    return
