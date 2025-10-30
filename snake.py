from point import Point
from enum import Enum

class Heading(Enum):
    NORTH = Point(0, 1)
    EAST = Point(1, 0)
    SOUTH = Point(0, -1)
    WEST = Point(-1, 0)

def no_disconnects(points: list[Point]) -> bool:
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        diff = abs(x1 - x0) + abs(y1 - y0)
        if diff > 1:
            return False
    return True

class Snake:
    _segments: list[Point]
    _heading: Heading

    def __init__(self, segments: list[Point] = None, heading: Heading = Heading.EAST) -> None:
        if segments is None:
            segments = [Point(0, 0)]

        if segments == []:
            raise ValueError(f"Invalid segments argument: empty list")

        if not no_disconnects(segments):
            raise ValueError(f"Invalid segments argument: disconnect segments")

        self._segments = list(segments)
        self._heading = heading

    @property
    def segments(self) -> list[Point, ...]:
        return list(self._segments)

    @property
    def length(self) -> int:
        return len(self._segments)

    @property
    def head(self) -> Point:
        return self._segments[0]

    @property
    def tail(self) -> Point:
        return self._segments[-1]

    @property
    def heading(self) -> Heading:
        return self._heading

    def grow(self) -> None:
        self._segments.append(self._segments[-1])

    def move(self) -> None:
        head = self.head
        head = Point(head.x + self._heading.value.x, head.y + self._heading.value.y)
        self._segments.pop(-1)
        self._segments.insert(0, head)

    def turn(self, heading: Heading) -> bool:
        opposite = Point(heading.value.x * -1, heading.value.y * -1)
        if self._heading.value == opposite:
            return False
        self._heading = heading
        return True

    def head_colliding_with_body(self) -> bool:
        for body in self._segments[1:]:
            if self.head == body:
                return True
        return False
