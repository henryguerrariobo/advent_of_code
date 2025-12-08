"""Archivo main del data-science-template."""

from __future__ import annotations

import logging

from advent_of_code.analyze import analyze_data
from advent_of_code.config import ProjectConfig, load_config
from advent_of_code.export import export_results
from advent_of_code.load import load_data
from advent_of_code.process import process_data


def config_logging() -> None:
    """
    Configuración de logging.

    Configura el nivel de logging y los formatos para los mensajes de log.
    """
    logging.basicConfig(
        # level=logging.INFO,
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # logging.getLogger("fastexcel").setLevel(logging.ERROR)
    logging.getLogger("office365").setLevel(logging.ERROR)


def run() -> None:
    """
    Partes del proyecto de análisis de datos.

    Carga la configuración y los datos, los procesa y exporta los resultados.
    """
    config_logging()
    config: ProjectConfig = load_config("main.json")

    logging.info("Iniciando el análisis con la configuración: %s", config)

    load_data(execute_module=True, config=config)
    process_data(execute_module=True, config=config)
    analyze_data(execute_module=True, config=config)
    export_results(execute_module=True, config=config)

    print("Finalizando el análisis")


if __name__ == "__main__":
    run()
