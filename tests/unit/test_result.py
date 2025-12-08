"""Tests para el módulo result."""

from __future__ import annotations

import pytest

from advent_of_code.result import Err, Ok, Result, try_call


class TestResultBasics:
    """Tests básicos para Result, Ok y Err."""

    def test_ok_creation(self) -> None:
        """Test creación de Ok."""
        result = Ok(42)
        assert result.value == 42
        assert str(result) == "Ok(42)"
        assert repr(result) == "Ok(42)"

    def test_err_creation(self) -> None:
        """Test creación de Err."""
        result = Err("error message")
        assert result.error == "error message"
        assert str(result) == "Err(error message)"
        assert repr(result) == "Err('error message')"

    def test_ok_is_ok(self) -> None:
        """Test que Ok es Ok."""
        result = Ok(42)
        assert result.is_ok() is True
        assert result.is_err() is False

    def test_err_is_err(self) -> None:
        """Test que Err es Err."""
        result = Err("error")
        assert result.is_ok() is False
        assert result.is_err() is True

    def test_ok_equality(self) -> None:
        """Test igualdad de Ok."""
        assert Ok(42) == Ok(42)
        assert Ok(42) != Ok(43)
        assert Ok(42) != Err("error")

    def test_err_equality(self) -> None:
        """Test igualdad de Err."""
        assert Err("error") == Err("error")
        assert Err("error1") != Err("error2")
        assert Err("error") != Ok(42)


class TestResultUnwrap:
    """Tests para métodos de unwrap."""

    def test_ok_unwrap(self) -> None:
        """Test unwrap de Ok retorna valor."""
        result = Ok(42)
        assert result.unwrap() == 42

    def test_err_unwrap_raises(self) -> None:
        """Test unwrap de Err lanza excepción."""
        result = Err("error message")
        with pytest.raises(RuntimeError, match="Called unwrap on Err: error message"):
            result.unwrap()

    def test_ok_unwrap_or(self) -> None:
        """Test unwrap_or de Ok retorna valor."""
        result = Ok(42)
        assert result.unwrap_or(0) == 42

    def test_err_unwrap_or(self) -> None:
        """Test unwrap_or de Err retorna default."""
        result = Err("error")
        assert result.unwrap_or(0) == 0


class TestTryCall:
    """Tests para la función try_call."""

    def test_try_call_success(self) -> None:
        """Test try_call con función exitosa."""
        result = try_call(lambda: 42)
        assert result == Ok(42)

    def test_try_call_exception(self) -> None:
        """Test try_call con función que lanza excepción."""
        result = try_call(lambda: int("not a number"))
        assert result.is_err()
        assert isinstance(result.error, ValueError)

    def test_try_call_specific_exception(self) -> None:
        """Test try_call captura except específica."""

        def divide_by_zero() -> float:
            return 1 / 0

        result = try_call(divide_by_zero)
        assert result.is_err()
        assert isinstance(result.error, ZeroDivisionError)

    def test_try_call_with_side_effects(self) -> None:
        """Test try_call con efectos secundarios."""
        side_effect_list = []

        def function_with_side_effect() -> int:
            side_effect_list.append("executed")
            return 42

        result = try_call(function_with_side_effect)
        assert result == Ok(42)
        assert side_effect_list == ["executed"]


class TestResultPatternMatching:
    """Tests para pattern matching con Results."""

    def test_pattern_matching_ok(self) -> None:
        """Test pattern matching con Ok."""
        result = Ok(42)

        match result:
            case Ok(value):
                assert value == 42
            case Err(error):
                pytest.fail(f"Should not match Err: {error}")

    def test_pattern_matching_err(self) -> None:
        """Test pattern matching con Err."""
        result = Err("error message")

        match result:
            case Ok(value):
                pytest.fail(f"Should not match Ok: {value}")
            case Err(error):
                assert error == "error message"

    def test_pattern_matching_in_function(self) -> None:
        """Test pattern matching en función."""

        def process_result(result: Result[int, str]) -> str:
            match result:
                case Ok(value):
                    return f"Success: {value}"
                case Err(error):
                    return f"Error: {error}"

        assert process_result(Ok(42)) == "Success: 42"
        assert process_result(Err("failed")) == "Error: failed"
