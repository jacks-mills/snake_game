from snake import Snake, Heading
from point import Point
import random

class BoardState:
    _width: int
    _height: int

    _snake: Snake
    _apple: Point | None

    _availableAppleSpaces: set[Point]


    def __init__(self, width: int = 15, height: int = 15) -> None:
        head = Point(width//2, height//2)
        self._snake = Snake([head], Heading.EAST)

        self._availableAppleSpaces = {Point(x, y) for x in range(width) for y in range(height)}
        self._availableAppleSpaces.remove(head)
        self._apple = self._new_apple()

        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def snake(self) -> Snake:
        return self._snake

    @property
    def apple(self) -> Point | None:
        return self._apple

    def _new_apple(self) -> Point | None:
        if len(self._availableAppleSpaces) == 0:
            return None
        return random.sample(self._availableAppleSpaces, 1)[0]
    
    def _snake_in_bounds(self) -> bool:
        return 0 <= self._snake.head.x < self._width and 0 <= self._snake.head.y < self._height

    def step(self, heading: Heading | None) -> None:
        if heading is not None:
            self._snake.turn(heading)

        self._availableAppleSpaces.add(self._snake.tail)
        self._snake.move()

        if self._snake.head_colliding_with_body():
            raise NotImplementedError("Game over")

        if not self._snake_in_bounds():
            raise NotImplementedError("Game over")

        self._availableAppleSpaces.remove(self._snake.head)
        self._availableAppleSpaces.discard(self._snake.tail) # if _snake grew last step, need to remove tail

        if self._snake.head == self._apple:
            self._snake.grow()

            if self._snake.length == self._width * self._height:
                raise NotImplementedError("Game won")

            self._apple = self._new_apple()

    
