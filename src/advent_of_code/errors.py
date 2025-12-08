"""Módulo de manejo de errores para el dominio de Incrementos Salariales."""

from __future__ import annotations

from pathlib import Path


class DomainError(Exception):
    """Clase base para todos los errores del dominio."""

    def __init__(self, message: str = "Ha ocurrido un error en el dominio."):
        """Inicializa el exception con un mensaje por defecto."""
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """Representación en cadena del error."""
        return self.message


# ────── Errores de Carga de Archivos ──────


class FileNotFound(DomainError):
    """Archivo no encontrado en la ruta especificada."""

    def __init__(self, path: Path, cause: Exception):
        """Inicializa el error con la ruta del archivo no encontrado."""
        self.path = path
        self.cause = cause  # para mantener el traceback original

        message = f"Archivo no encontrado: '{path}'"
        if cause is not None:
            message += f" | Causa original: {type(cause).__name__}: {cause}"

        super().__init__(message)


class FilePermissionDenied(DomainError):
    """Permisos insuficientes para acceder al archivo."""

    def __init__(self, path: Path, cause: Exception):
        """Inicializa el error con la ruta del archivo denegado."""
        self.path = path
        self.cause = cause  # para mantener el traceback original

        message = f"Permiso denegado para acceder a: '{path}'"
        if cause is not None:
            message += f" | Causa original: {type(cause).__name__}: {cause}"

        super().__init__(message)


class InvalidFileFormat(DomainError):
    """El archivo tiene un formato inválido o no soportado."""

    def __init__(self, path: Path, expected_format: str, cause: Exception):
        """Inicializa el error con la ruta y formato esperado."""
        self.path = path
        self.expected_format = expected_format
        self.cause = cause  # para mantener el traceback original

        message = f"Formato inválido en {path}. Se esperaba: {expected_format}"
        if cause is not None:
            message += f" | Causa original: {type(cause).__name__}: {cause}"

        super().__init__(message)
