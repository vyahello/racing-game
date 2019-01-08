import os
from enum import Enum
from typing import Iterable

_images: str = os.path.join('lib/images/')


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

    car: str = f'{_images}car.jpg'
    car_one: str = f'{_images}car1.jpg'
    car_two: str = f'{_images}car2.jpg'
    car_three: str = f'{_images}car3.jpg'
    car_four: str = f'{_images}car4.jpg'
    car_five: str = f'{_images}car5.jpg'
    car_six: str = f'{_images}car6.jpg'
    grass: str = f'{_images}grass.jpg'
    yellow_strip: str = f'{_images}yellow_strip.jpg'
    strip: str = f'{_images}strip.jpg'
    back: str = f'{_images}back.jpg'
    back_alternative: str = f'{_images}back_alternative.jpg'
