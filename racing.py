from typing import Tuple
import pygame
import time
import random
from lib.game.display import GameDisplay, Clock
from lib.game.engines import GameEngine
from lib.game.events import events
from lib.game.images import GameImages
from lib.game.navigation import Navigation
from lib.game.properties import Colors, Display, Images, Car

PAUSE = False


class _GameSetup:
    """The class represents setup for a game."""

    GAME = GameEngine()
    DISPLAY = GameDisplay(Display)
    CLOCK = Clock()
    GAME_IMAGES = GameImages(Images)
    GAME_DISPLAYS = DISPLAY.set_size()
    DISPLAY.set_title()
    CAR_IMAGE = GAME_IMAGES.car()
    BACKGROUND_PIC = GAME_IMAGES.grass()
    YELLOW_STRIP = GAME_IMAGES.yellow_strip()
    STRIP = GAME_IMAGES.strip()
    INTRO_BACKGROUND = GAME_IMAGES.back()
    INSTRUCTION_BACKGROUND = GAME_IMAGES.back_alter()


class _GameView:
    """The class represents game view."""

    GRAY = Colors.gray.value
    BLACK = Colors.black.value
    RED = Colors.red.value
    GREEN = Colors.green.value
    BLUE = Colors.blue.value
    BRIGHT_RED = Colors.bright_red.value
    BRIGHT_GREEN = Colors.bright_green.value
    BRIGHT_BLUE = Colors.bright_blue.value
    DISPLAY_WIDTH = Display.width.value
    DISPLAY_HEIGHT = Display.height.value


def intro_loop() -> None:
    """Runs into game loop."""
    while True:
        for event in events():
            if event.type == Navigation.is_quit(event):
                _GameSetup.GAME.stop()
        _GameSetup.GAME_DISPLAYS.blit(_GameSetup.INTRO_BACKGROUND, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 90)
        text_surf, text_rect = text_objects("RACING GAME", large_text)
        text_rect.center = (400, 100)
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        button("START", 150, 520, 100, 50, _GameView.GREEN, _GameView.BRIGHT_GREEN, "play")
        button("QUIT", 550, 520, 100, 50, _GameView.RED, _GameView.BRIGHT_RED, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, _GameView.BLUE, _GameView.BRIGHT_BLUE, "intro")
        pygame.display.update()
        _GameSetup.CLOCK.tick(50)


def button(message, x_coordinate, y_coordinate, weight, height, from_color, back_color, action=None) -> None:
    """Returns a game button."""
    mouse = Navigation.get_mouse_position()
    click = Navigation.get_mouse_pressed()
    if x_coordinate + weight > mouse[0] > x_coordinate and y_coordinate + height > mouse[1] > y_coordinate:
        pygame.draw.rect(_GameSetup.GAME_DISPLAYS, back_color, (x_coordinate, y_coordinate, weight, height))
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "quit":
                _GameSetup.GAME.stop()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                pause_game()
            elif action == "unpause":
                unpause_game()
    else:
        pygame.draw.rect(_GameSetup.GAME_DISPLAYS, from_color, (x_coordinate, y_coordinate, weight, height))
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(message, small_text)
    text_rect.center = ((x_coordinate + (weight / 2)), (y_coordinate + (height / 2)))
    _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)


def introduction() -> None:
    """Displays game introduction."""
    while True:
        for event in events():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

        _GameSetup.GAME_DISPLAYS.blit(_GameSetup.INSTRUCTION_BACKGROUND, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 80)
        small_text = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        text_surf, text_rect = text_objects("This is an car game in which you need dodge the coming cars", small_text)
        text_rect.center = (350, 200)
        text_surf, text_rect = text_objects("INSTRUCTION", large_text)
        text_rect.center = (400, 100)
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        s_text_surf, s_text_rect = text_objects("ARROW LEFT : LEFT TURN", small_text)
        s_text_rect.center = (150, 400)
        h_text_surf, h_text_rect = text_objects("ARROW RIGHT : RIGHT TURN", small_text)
        h_text_rect.center = (150, 450)
        a_text_surf, a_text_rect = text_objects("A : ACCELERATOR", small_text)
        a_text_rect.center = (150, 500)
        r_text_surf, r_text_rect = text_objects("B : BRAKE ", small_text)
        r_text_rect.center = (150, 550)
        p_text_surf, p_text_rect = text_objects("P : PAUSE  ", small_text)
        p_text_rect.center = (150, 350)
        s_text_surf, s_text_rect = text_objects("CONTROLS", mediumtext)
        s_text_rect.center = (350, 300)
        _GameSetup.GAME_DISPLAYS.blit(s_text_surf, s_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(s_text_surf, s_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(h_text_surf, h_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(a_text_surf, a_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(r_text_surf, r_text_rect)
        _GameSetup.GAME_DISPLAYS.blit(p_text_surf, p_text_rect)
        button("BACK", 600, 450, 100, 50, _GameView.BLUE, _GameView.BRIGHT_BLUE, "menu")
        pygame.display.update()
        _GameSetup.CLOCK.tick(30)


def pause_game() -> None:
    """Pause a game."""
    global PAUSE
    while PAUSE:
        for event in events():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

        _GameSetup.GAME_DISPLAYS.blit(_GameSetup.INSTRUCTION_BACKGROUND, (0, 0))
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("PAUSED", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        button("CONTINUE", 150, 450, 150, 50, _GameView.GREEN, _GameView.BRIGHT_GREEN, "unpause")
        button("RESTART", 350, 450, 150, 50, _GameView.BLUE, _GameView.BRIGHT_BLUE, "play")
        button("MAIN MENU", 550, 450, 200, 50, _GameView.RED, _GameView.BRIGHT_RED, "menu")
        pygame.display.update()
        _GameSetup.CLOCK.tick(30)


def unpause_game() -> None:
    """Unpause a game."""
    global PAUSE
    PAUSE = False


def countdown_background() -> None:
    """Displays game background."""
    font = pygame.font.SysFont(None, 25)
    x = (_GameView.DISPLAY_WIDTH * 0.45)
    y = (_GameView.DISPLAY_HEIGHT * 0.8)
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 300))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 500))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 600))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.CAR_IMAGE, (x, y))
    text = font.render("DODGED: 0", True, _GameView.BLACK)
    score = font.render("SCORE: 0", True, _GameView.RED)
    _GameSetup.GAME_DISPLAYS.blit(text, (0, 50))
    _GameSetup.GAME_DISPLAYS.blit(score, (0, 30))
    button("PAUSE", 650, 0, 150, 50, _GameView.BLUE, _GameView.BRIGHT_BLUE, "pause")


def countdown() -> None:
    """Counts down game loop."""
    while True:
        for event in events():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("3", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("2", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("1", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)
        countdown_background()
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("GO!!!", large_text)
        text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
        _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
        pygame.display.update()
        _GameSetup.CLOCK.tick(1)
        game_loop()


def obstacle(obs_start_x: int, obs_start_y: int, obs: int) -> None:
    """Visualize some game canvas obstacle."""
    images = {
        0: _GameSetup.GAME_IMAGES.car(),
        1: _GameSetup.GAME_IMAGES.car_one(),
        2: _GameSetup.GAME_IMAGES.car_two(),
        3: _GameSetup.GAME_IMAGES.car_three(),
        4: _GameSetup.GAME_IMAGES.car_four(),
        5: _GameSetup.GAME_IMAGES.car_five(),
        6: _GameSetup.GAME_IMAGES.car_six()
    }
    _GameSetup.GAME_DISPLAYS.blit(images[obs], (obs_start_x, obs_start_y))


def score_system(passed: str, score: int) -> None:
    """Displays scoring table."""
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed" + str(passed), True, _GameView.BLACK)
    score = font.render("Score" + str(score), True, _GameView.RED)
    _GameSetup.GAME_DISPLAYS.blit(text, (0, 50))
    _GameSetup.GAME_DISPLAYS.blit(score, (0, 30))


def text_objects(text: str, font: pygame.font.Font) -> Tuple[str, str]:
    """Returns some text object."""
    text_surface = font.render(text, True, _GameView.BLACK)
    return text_surface, text_surface.get_rect()


def message_display(text: str) -> None:
    """Displays some message."""
    large_text = pygame.font.Font("freesansbold.ttf", 80)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
    _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash() -> None:
    """Displays crash message."""
    message_display("YOU CRASHED")


def background() -> None:
    """Displays background on the canvas."""
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 300))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 400))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, 500))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, 200))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 0))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 100))
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, 200))


def display_car(x_coordinate: int, y_coordinate: int) -> None:
    """Displays car on the canvas."""
    _GameSetup.GAME_DISPLAYS.blit(_GameSetup.CAR_IMAGE, (x_coordinate, y_coordinate))


def game_loop() -> None:
    """Starts main game loop."""
    global PAUSE
    x = (_GameView.DISPLAY_WIDTH * 0.45)
    y = (_GameView.DISPLAY_HEIGHT * 0.8)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    obs_start_x = random.randrange(200, (_GameView.DISPLAY_WIDTH - 200))
    obs_start_y = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if Navigation.is_quit(event):
                _GameSetup.GAME.stop()

            if Navigation.is_down(event):
                if Navigation.is_left(event):
                    x_change = -5
                if Navigation.is_right(event):
                    x_change = 5
                if Navigation.is_a(event):
                    obstacle_speed += 2
                if Navigation.is_b(event):
                    obstacle_speed -= 2
            if Navigation.is_up(event):
                if Navigation.is_left(event) or Navigation.is_right(event):
                    x_change = 0

        x += x_change
        PAUSE = True
        _GameSetup.GAME_DISPLAYS.fill(_GameView.GRAY)

        rel_y = y2 % _GameSetup.BACKGROUND_PIC.get_rect().width
        _GameSetup.GAME_DISPLAYS.blit(
            _GameSetup.BACKGROUND_PIC, (0, rel_y - _GameSetup.BACKGROUND_PIC.get_rect().width)
        )
        _GameSetup.GAME_DISPLAYS.blit(
            _GameSetup.BACKGROUND_PIC, (700, rel_y - _GameSetup.BACKGROUND_PIC.get_rect().width)
        )
        if rel_y < 800:
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (0, rel_y))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.BACKGROUND_PIC, (700, rel_y))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y + 100))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y + 200))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y + 300))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y + 400))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y + 500))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.YELLOW_STRIP, (400, rel_y - 100))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, rel_y - 200))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, rel_y + 20))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (120, rel_y + 30))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, rel_y - 100))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, rel_y + 20))
            _GameSetup.GAME_DISPLAYS.blit(_GameSetup.STRIP, (680, rel_y + 30))

        y2 += obstacle_speed

        obs_start_y -= (obstacle_speed / 4)
        obstacle(obs_start_x, obs_start_y, obs)
        obs_start_y += obstacle_speed
        display_car(x, y)
        score_system(passed, score)
        if x > 690 - Car.width.value or x < 110:
            crash()
        if x > _GameView.DISPLAY_WIDTH - (Car.width.value + 110) or x < 110:
            crash()
        if obs_start_y > _GameView.DISPLAY_HEIGHT:
            obs_start_y = 0 - obs_height
            obs_start_x = random.randrange(170, (_GameView.DISPLAY_WIDTH - 170))
            obs = random.randrange(0, 7)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed + 2
                large_text = pygame.font.Font("freesansbold.ttf", 80)
                text_surf, text_rect = text_objects("LEVEL" + str(level), large_text)
                text_rect.center = ((_GameView.DISPLAY_WIDTH / 2), (_GameView.DISPLAY_HEIGHT / 2))
                _GameSetup.GAME_DISPLAYS.blit(text_surf, text_rect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_start_y + obs_height:
            if obs_start_x < x < obs_start_x + obs_width or obs_start_x < x + Car.width.value < obs_start_x + obs_width:
                crash()
        button("Pause", 650, 0, 150, 50, _GameView.BLUE, _GameView.BRIGHT_BLUE, "pause")
        pygame.display.update()
        _GameSetup.CLOCK.tick(60)


def _run_game() -> None:
    """Starts game runner."""
    _GameSetup.GAME.start()
    intro_loop()
    game_loop()
    _GameSetup.GAME.stop()


if __name__ == "__main__":
    _run_game()
