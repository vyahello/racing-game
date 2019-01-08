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
    caption: str = 'Racing Game'


class Images(Enum):
    """Represent game images."""

    car: str = 'car.jpg'
    car_one: str = 'car1.jpg'
    car_two: str = 'car2.jpg'
    car_three: str = 'car3.jpg'
    car_four: str = 'car4.jpg'
    car_five: str = 'car5.jpg'
    car_six: str = 'car6.jpg'
    grass: str = 'grass.jpg'
    yellow_strip: str = 'yellow_strip.jpg'
    strip: str = 'strip.jpg'
    back: str = 'back.jpg'
    back_alternative: str = 'back_alternative.jpg'
