"""En este módulo se descargan los datos de la fuente de datos."""

from __future__ import annotations

import logging

from advent_of_code.config import ProjectConfig


def export_results(execute_module: bool, config: ProjectConfig) -> None:
    """Exportando los datos."""
    if not execute_module:
        logging.info("⏭️ Módulo ANALYZE deshabilitado, omitiendo análisis de datos")
        return

    print("Exportando los datos", config)

    return
