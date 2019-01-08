from typing import Type
from pygame import display, time, Surface
from lib.game.properties import Display


class GameDisplay:
    """Display of a game."""

    def __init__(self, option: Type[Display]) -> None:
        self._option = option
        self._display = display

    def set_title(self) -> None:
        self._display.set_caption(Display.caption.value)

    def set_size(self) -> Surface:
        return self._display.set_mode(
            (
                Display.width.value,
                Display.height.value
            )
        )


class Clock:
    """Game time clock."""

    def __init__(self) -> None:
        self._clock: time.Clock = time.Clock()

    def tick(self, seconds: int) -> int:
        return self._clock.tick(seconds)
