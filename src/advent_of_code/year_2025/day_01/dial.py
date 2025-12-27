"""
Módulo que define la clase Dial.

Contiene la lógica para simular el movimiento del dial y
contar cuántas veces termina apuntando a la posición 0.
"""

from __future__ import annotations

__all__ = ["Dial"]


class Dial:
    """
    Representa el dial del cofre de seguridad.

    El dial comienza en una posición inicial y puede rotar
    a la izquierda o a la derecha según las instrucciones.
    """

    def __init__(self, start_position: int = 50):
        """
        Inicializa el dial.

        Args:
            start_position (int): Posición inicial del dial.

        """
        self.position_initial = start_position
        self.count_zero = 0

    def run_dial(self, instruction: tuple[str, int]) -> None:
        """
        Ejecuta una instrucción sobre el dial.

        Actualiza la posición del dial según la instrucción
        recibida y cuenta cuántas veces la posición final es 0.

        Args:
            instruction (tuple[str, int]): Tupla con la dirección
                ('L' o 'R') y la cantidad de pasos.

        """
        letra, valor = instruction

        if letra == "L":
            self.position_initial -= valor
        elif letra == "R":
            self.position_initial += valor

        self.position_initial %= 100

        if self.position_initial == 0:
            self.count_zero += 1

    def run_dial_part_two(self, instruction: tuple[str, int]) -> None:
        """
        Ejecuta una instrucción sobre el dial.

        Actualiza la posición del dial según la instrucción
        recibida y cuenta cuántas veces el contador pasa por 0.

        Args:
            instruction (tuple[str, int]): Tupla con la dirección
                ('L' o 'R') y la cantidad de pasos.

        """
        letra, valor = instruction

        for _ in range(valor):
            if letra == "L":
                self.position_initial -= 1
            elif letra == "R":
                self.position_initial += 1

            self.position_initial %= 100

            if self.position_initial == 0:
                self.count_zero += 1
