from enum import Enum
from typing import Iterable


class Colors(Enum):
    """Represent set of colors for a game"""

    gray: Iterable[int] = (
        119,
        118,
        110
    )
    black: Iterable[int] = (
        0,
        0,
        0
    )
    red: Iterable[int] = (
        255,
        0,
        0
    )
    green: Iterable[int] = (
        0,
        200,
        0
    )
    blue: Iterable[int] = (
        0,
        0,
        200
    )
    bright_red: Iterable[int] = (
        255,
        0,
        0
    )
    bright_green: Iterable[int] = (
        0,
        255,
        0
    )
    bright_blue: Iterable[int] = (
        0,
        0,
        255
    )


class Display(Enum):
    """Represent display properties."""

    width: int = 800
    height: int = 600
