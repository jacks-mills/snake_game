from typing import NamedTuple
from enum import Enum
import random


class Point(NamedTuple):
    x: int
    y: int

class Heading(Enum):
    NORTH = Point(0, 1)
    SOUTH = Point(0, -1)
    EAST = Point(1, 0)
    WEST = Point(-1, 0)

class BoardState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    GAME_WON = 3

class Board:
    width: int
    height: int

    snake: list[Point]
    heading: Heading
    fruit: Point | None

    newHeading: Heading | None
    state: BoardState


    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.snake = [Point(self.width//2, self.height//2)]
        self.heading = Heading.NORTH
        self.fruit = self.new_fruit()

        self.newState = None
        self.state = BoardState.PLAYING

    def new_fruit(self) -> Point | None:
        if len(self.snake) == self.width * self.height:
            return None
        available = [Point(x, y) for x in range(self.width) for y in range(self.height) if Point(x, y) not in self.snake]
        return random.choice(available)
    
    def set_new_heading(self, heading: Heading | None) -> None:
        self.newHeading = heading

    def step(self) -> None:
        if self.state != BoardState.PLAYING:
            return
        
        if self.newHeading is not None:
            opposite = Point(-self.heading.value.x, -self.heading.value.y)
            if opposite != self.newHeading.value:
                self.heading = self.newHeading
            self.newHeading = None

        head = self.snake[0]
        newHead = Point(head.x + self.heading.value.x, head.y + self.heading.value.y)

        # check if out of bounds
        if newHead.x < 0 or self.width <= newHead.x or newHead.y < 0 or self.height <= newHead.y:
            self.state = BoardState.GAME_OVER
            return

        # check for body collision
        for segment in self.snake[:-1]:
            if newHead == segment:
                self.state = BoardState.GAME_OVER
                return

        self.snake.insert(0, newHead)
        self.snake.pop(-1)

        if newHead == self.fruit:
            self.snake.append(self.snake[-1])

            if len(self.snake) == self.width * self.height:
                self.state = BoardState.GAME_WON
                self.fruit = None
                return

            self.fruit = self.new_fruit()


    
