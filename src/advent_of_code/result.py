"""
Result pattern implementation for robust error handling.

Implementación minimalista del patrón Result para manejo explícito de errores
sin dependencia en excepciones automáticas.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import cast


class Result[T, E]:
    """
    Patrón Result para manejo explícito de errores.

    Result representa el resultado de una operación que puede fallar.
    Puede ser Ok(value) para éxito o Err(error) para fallo.
    """

    def is_ok(self) -> bool:
        """Retorna True si el resultado es Ok."""
        return isinstance(self, Ok)

    def is_err(self) -> bool:
        """Retorna True si el resultado es Err."""
        return isinstance(self, Err)

    def unwrap(self) -> T:
        """
        Extrae el valor si es Ok, lanza excepción si es Err.

        Returns:
            El valor contenido si es Ok

        Raises:
            RuntimeError: Si el resultado es Err

        """
        if isinstance(self, Ok):
            return cast(T, self.value)

        msg = f"Called unwrap on Err: {self.error}"
        raise RuntimeError(msg)

    def unwrap_err(self) -> E:
        """
        Extrae el error si es Err, lanza excepción si es Ok.

        Returns:
            El error contenido si es Err

        Raises:
            RuntimeError: Si el resultado es Ok

        """
        if isinstance(self, Err):
            return cast(E, self.error)

        msg = f"Called unwrap_err on Ok: {self.value}"
        raise RuntimeError(msg)

    def unwrap_or(self, default: T) -> T:
        """
        Extrae el valor si es Ok, retorna default si es Err.

        Args:
            default: Valor por defecto si es Err

        Returns:
            El valor contenido o el valor por defecto

        """
        if isinstance(self, Ok):
            return cast(T, self.value)

        return default


@dataclass
class Ok[T, E](Result[T, E]):
    """Representa un resultado exitoso con un valor."""

    __match_args__ = ("value",)

    def __init__(self, value: T):
        """Inicializa un resultado Ok con un valor."""
        self.value = value

    def __str__(self) -> str:
        """Representación en cadena del resultado Ok."""
        return f"Ok({self.value})"

    def __repr__(self) -> str:
        """Representación detallada del resultado Ok."""
        return f"Ok({repr(self.value)})"

    def __eq__(self, other: object) -> bool:
        """Compara si dos resultados Ok son iguales."""
        return isinstance(other, Ok) and self.value == other.value

    def __hash__(self) -> int:
        """Hash del resultado Ok basado en su valor."""
        return hash(("Ok", self.value))


@dataclass
class Err[T, E](Result[T, E]):
    """Representa un resultado con error."""

    __match_args__ = ("error",)

    def __init__(self, error: E):
        """Inicializa un resultado Err con un mensaje de error."""
        self.error = error

    def __str__(self) -> str:
        """Representación en cadena del resultado Err."""
        return f"Err({self.error})"

    def __repr__(self) -> str:
        """Representación detallada del resultado Err."""
        return f"Err({repr(self.error)})"

    def __eq__(self, other: object) -> bool:
        """Compara si dos resultados Err son iguales."""
        return isinstance(other, Err) and self.error == other.error

    def __hash__(self) -> int:
        """Hash del resultado Err basado en su error."""
        return hash(("Err", self.error))


# =============================================================================
# UTILITY FUNCTIONS - Solo lo esencial
# =============================================================================


def try_call[T](f: Callable[[], T]) -> Result[T, Exception]:
    """
    Ejecuta función y convierte excepciones a Result.

    Usar SOLO en boundaries con librerías externas (Polars, Pandera, I/O).

    Args:
        f: Función a ejecutar sin argumentos

    Returns:
        Ok con resultado o Err con excepción capturada

    Example:
        >>> result = try_call(lambda: int("123"))
        >>> assert result == Ok(123)

        >>> result = try_call(lambda: int("abc"))
        >>> assert result.is_err()
        >>> isinstance(result.error, ValueError)
        True

    """
    try:
        return Ok(f())
    except Exception as e:
        return Err(e)
