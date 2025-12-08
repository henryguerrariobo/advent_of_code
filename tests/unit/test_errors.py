from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import fastexcel
import polars as pl
import pytest

from advent_of_code.errors import (
    FileNotFound,
    FilePermissionDenied,
    InvalidFileFormat,
)

# =============================================================================
# Tests para la excepción FileNotFound
# =============================================================================


def test_file_not_found_includes_error_real_exception():
    fake_path = Path("data/no_existe.xlsx")

    with pytest.raises(FileNotFoundError) as default_error:
        # Esto lanzará FileNotFoundError
        pl.read_excel(fake_path)

    # Envolvemos en nuestra excepción de dominio
    custom_error = FileNotFound(fake_path, cause=default_error)

    # Verifica que la causa esté almacenada
    assert custom_error.cause is default_error

    # Verifica que el mensaje incluya el error custom
    assert f"Archivo no encontrado: '{fake_path}'" in str(custom_error)

    # Verifica que el tipo de la causa sea FileNotFoundError
    err_lines = [
        "Causa original: ExceptionInfo: ",
        "<ExceptionInfo ",
        f"FileNotFoundError(\"no workbook found at path '{fake_path}'\") tblen=5>",
    ]
    except_err = "".join(err_lines)
    assert except_err in str(custom_error)


# =============================================================================
# Tests para la excepción FilePermissionDenied
# =============================================================================


def test_file_permission_denied_real_exception():
    test_folder = Path(tempfile.mkdtemp())

    # crear un archivo temporal
    temp_file = test_folder / "temp_file.txt"
    temp_file.touch()

    # Quitar permisos de lectura
    temp_file.chmod(0o000)

    with pytest.raises(PermissionError) as default_error:
        # Intentar abrir el archivo sin permisos
        temp_file.open("r")

    # Envolver en excepción de dominio
    custom_error = FilePermissionDenied(temp_file, cause=default_error)

    # Verifica que la causa esté almacenada
    assert custom_error.cause is default_error

    # Verifica que el mensaje incluya el error custom
    assert f"Permiso denegado para acceder a: '{temp_file}'" in str(custom_error)

    # Verifica que el tipo de la causa sea FileNotFoundError
    err_lines = [
        # Causa original: ExceptionInfo: <ExceptionInfo >
        "Causa original: ExceptionInfo: ",
        "<ExceptionInfo ",
        "PermissionError(13, 'Permission denied') tblen=2>",
    ]
    except_err = "".join(err_lines)
    assert except_err in str(custom_error)

    shutil.rmtree(test_folder)


# =============================================================================
# Tests para la excepción InvalidFileFormat
# =============================================================================


def test_invalid_file_format_real_exception_with_invalid_content():
    test_folder = Path(tempfile.mkdtemp())

    # crear un archivo temporal
    temp_file = test_folder / "temp_file.xlsx"
    temp_file.touch()
    temp_file.write_text("esto no es un archivo Excel válido")

    with pytest.raises(fastexcel.CalamineError) as default_error:
        # Esto debería lanzar un error de formato
        pl.read_excel(temp_file)

    # Envolver en excepción de dominio
    custom_error = InvalidFileFormat(
        path=temp_file, expected_format="Excel", cause=default_error
    )

    print("original", default_error)
    print("custom", custom_error)

    # Verifica que la causa esté almacenada
    assert custom_error.cause is default_error

    # Verifica que el mensaje incluya el error custom
    assert f"Formato inválido en {temp_file}. Se esperaba: Excel" in str(custom_error)
    assert "Causa original: ExceptionInfo:" in str(custom_error)
    assert "CalamineError" in str(custom_error)
    assert "invalid Zip archive" in str(custom_error)
    # assert "No valid central directory found" in str(custom_error)

    shutil.rmtree(test_folder)
