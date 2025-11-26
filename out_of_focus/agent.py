from snake import Snake, Heading
from point import Point
from game import Game
from collections.abc import Iterable
from typing import TypeVar
import random
from ui import UI
from turtle_ui import TurtlePathVisualiser


class Agent:

    def __init__(self, game: Game, ui: UI) -> None:
        self.game = game
        self.ui = ui

        # will need some way of creating a visualiser from given UI
        self.visualiser = TurtlePathVisualiser(ui)

    def move(self) -> None:
        heading = self.game.snake.heading
        head = self.game.snake.head
        apple = self.game.apple

        if head.x > apple.x and head.y > apple.y:
            ...

        if head.x < apple.x and head.y > apple.y:
            ...

        if head.x < apple.x and head.y < apple.y:
            ...

        if head.x > apple.x and head.y < apple.y:
            ...


        raise ValueError("Unexpected Heading")
