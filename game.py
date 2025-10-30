from snake import Snake, Heading
from point import Point
from enum import Enum
from ui import UI
import random

class Game:
    snake: Snake
    apple: Point | None

    width: int
    height: int

    #state: State

    newHeading: Heading | None
    availableAppleSpaces: set[Point]


    def __init__(self, width: int = 15, height: int = 15) -> None:
        head = Point(width//2, height//2)
        self.snake = Snake([head], Heading.EAST)
        self.newHeading = None

        self.availableAppleSpaces = {Point(x, y) for x in range(width) for y in range(height)}
        self.availableAppleSpaces.remove(head)
        self.apple = self.new_apple()

        self.width = width
        self.height = height

    def new_apple(self) -> Point | None:
        if len(self.availableAppleSpaces) == 0:
            return None
        return random.sample(self.availableAppleSpaces, 1)[0]
    
    def set_new_heading(self, heading: Heading | None) -> None:
        self.newHeading = heading
        print(self.newHeading)

    def snake_in_bounds(self) -> bool:
        return 0 <= self.snake.head.x < self.width and 0 <= self.snake.head.y < self.height

    def step(self) -> None:
        if self.newHeading is not None:
            self.snake.turn(self.newHeading)
            self.newHeading = None

        self.availableAppleSpaces.add(self.snake.tail)
        self.snake.move()

        if self.snake.head_colliding_with_body():
            raise NotImplementedError("Game over")

        if not self.snake_in_bounds():
            raise NotImplementedError("Game over")

        self.availableAppleSpaces.remove(self.snake.head)
        self.availableAppleSpaces.discard(self.snake.tail) # if snake grew, need to remove tail

        if self.snake.head == self.apple:
            self.snake.grow()

            if self.snake.length == self.width * self.height:
                raise NotImplementedError("Game won")

            self.apple = self.new_apple()

def update_ui(ui: UI, game: Game) -> None:
    ui.erase_all()

    for body in game.snake.segments[1:]:
        ui.draw_snake_body(*body)
    ui.draw_snake_head(*game.snake.head)

    if game.apple is not None:
        ui.draw_apple(*game.apple)
    
