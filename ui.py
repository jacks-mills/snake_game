from board import Board, Point
from abc import ABC, abstractmethod

class UI(ABC):
    """
    Interface for snake game UI
    """

    @abstractmethod
    def draw_fruit(self, x: int, y: int) -> None:
        ...

    @abstractmethod
    def draw_snake_head(self, x: int, y: int) -> None:
        ...

    @abstractmethod
    def draw_snake_body(self, x: int, y: int) -> None:
        ...

    @abstractmethod
    def erase(self, x: int, y: int) -> None:
        ...

    @abstractmethod
    def erase_all(self) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        ...

class PathVisualiser(ABC):
    @abstractmethod
    def draw_path(self, points: list[Point], colour: str) -> int:
        ...

    @abstractmethod
    def erase(self, pid, int) -> None:
        ...

    @abstractmethod
    def erase_all(self) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        ...

