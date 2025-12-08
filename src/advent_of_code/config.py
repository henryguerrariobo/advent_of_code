"""Módulo para cargar la configuración para la ejecución."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from pydantic import BaseModel, ValidationError

from advent_of_code.errors import (
    DomainError,
    FileNotFound,
    FilePermissionDenied,
    InvalidFileFormat,
)
from advent_of_code.result import Err, Ok, Result

PROJECT_ROOT_PATH = Path(__file__).parents[2]
CONFIG_PATH = PROJECT_ROOT_PATH / "config"


class DataPaths(BaseModel):
    """
    Define las rutas donde se almacenan los datos en el proyecto.

    Attributes:
        raw (Path): Ruta a los datos sin procesar.
        process (Path): Ruta a los datos procesados.
        final (Path): Ruta a los datos finales.
        results (Path): Ruta a los resultados.

    """

    raw: Path
    process: Path
    final: Path
    results: Path


class ProjectConfig(BaseModel):
    """Representa la configuración completa del proyecto."""

    data: DataPaths
    # reports: Reports
    # params: Params


def read_json_file(file_path: Path) -> Result[str, DomainError]:
    """Cargar un archivo JSON con Result pattern."""
    try:
        with file_path.open() as file:
            data = json.load(file)
        logging.debug("✅ Archivo de configuración cargado: %s", file_path.name)
    except FileNotFoundError as e:
        logging.error("❌ Archivo de configuración no encontrado: %s", file_path)
        return Err(FileNotFound(file_path, cause=e))
    except PermissionError as e:
        logging.error(
            "❌ Permisos insuficientes para leer configuración: %s", file_path
        )
        return Err(FilePermissionDenied(file_path, cause=e))
    except json.JSONDecodeError as e:
        logging.error("❌ Error de formato JSON en configuración: %s", e)
        return Err(InvalidFileFormat(file_path, expected_format="JSON válido", cause=e))
    except Exception as e:
        logging.error("❌ Error inesperado leyendo configuración: %s", e)
        return Err(
            InvalidFileFormat(file_path, expected_format="archivo legible", cause=e)
        )

    # Filtrar las claves que son "_comment"
    filtered_dict = {k: v for k, v in data.items() if not k.startswith("_comment")}
    return Ok(json.dumps(filtered_dict))


def load_config(config_name: str, config_path: Path = CONFIG_PATH) -> ProjectConfig:
    """Cargar configuración de un JSON. Lanza excepciones si hay errores críticos."""
    logging.info("📄 Cargando configuración: %s", config_name)
    path_config: Path = config_path / config_name

    # Usar Result pattern para carga de archivo
    match read_json_file(path_config):
        case Ok(json_string):
            logging.debug("✅ JSON parseado exitosamente")
        case Err(error):
            logging.error(
                "❌ Error crítico cargando archivo de configuración: %s", error
            )
            raise error

    # Validar configuración con Pydantic
    try:
        config = ProjectConfig.model_validate_json(json_string)
        logging.info("✅ Configuración cargada y validada exitosamente")
        return config
    except ValidationError as e:
        logging.error("❌ Error de validación en configuración: %s", e)
        # Pydantic ValidationError ya tiene contexto detallado
        raise
    except Exception as e:
        logging.error("❌ Error inesperado validando configuración: %s", e)
        raise
