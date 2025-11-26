from turtle import Turtle, Screen
from ui import UI, PathVisualiser
from point import Point

def _make_turtle(colour: str = None, shape: str = None):
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.penup()

    if colour is not None:
        turt.color(colour)

    if shape is not None:
        turt.shape(shape)

    return turt

class TurtleUI(UI):
    """
    Inspired by code from https://www.geeksforgeeks.org/python/create-a-snake-game-using-turtle-in-python/
    """

    CELL_SIZE: int = 40
    #APPLE_SHAPE: tuple[tuple[float, float], ...] = ((0.0, 0.5), (-pow(3, 0.5)/4, -0.25), (pow(3, 0.5)/4, -0.25))
    APPLE_SHAPE: tuple[tuple[float, float], ...] = ((-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5))
    SNAKE_SHAPE: tuple[tuple[float, float], ...] = ((-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5))

    visibleStamps: dict[tuple[int, int], tuple[Turtle, int]]
    apple: Turtle
    head: Turtle
    body: Turtle

    screen: Screen

    def __init__(self, width: int, height: int) -> None:
        self.visibleStamps = {}
        self.apples = []
        self.heads = []
        self.bodies = []

        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.tracer(0)
        self.screen.setup(1.0, 1.0, startx=0.5, starty=0.5)
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")

        screenWidth = self.screen.window_width()
        screenHeight = self.screen.window_height()
        xShift = self.CELL_SIZE * (width - 1) / 2
        yShift = self.CELL_SIZE * (height - 1) / 2

        self.screen.setworldcoordinates(
                -screenWidth/2 + xShift, -screenHeight/2 + yShift, 
                 screenWidth/2 + xShift,  screenHeight/2 + yShift)

        appleShape = tuple((x * self.CELL_SIZE, y * self.CELL_SIZE) for x, y in self.APPLE_SHAPE)
        headShape = tuple((x * self.CELL_SIZE, y * self.CELL_SIZE) for x, y in self.SNAKE_SHAPE)
        bodyShape = headShape

        self.screen.register_shape("apple", appleShape)
        self.screen.register_shape("head", headShape)
        self.screen.register_shape("body", bodyShape)

        self.apple = _make_turtle("red", "apple")
        self.head = _make_turtle("white", "head")
        self.body = _make_turtle("orange", "body")

        self._draw_arena(self.CELL_SIZE * width, self.CELL_SIZE * height)

        self.screen.listen()
        self.screen.update()

    def draw_apple(self, x: int, y: int) -> None:
        self._draw_entity(self.apple, x, y)

    def draw_snake_head(self, x: int, y: int) -> None:
        self._draw_entity(self.head, x, y)

    def draw_snake_body(self, x: int, y: int) -> None:
        self._draw_entity(self.body, x, y)

    def erase(self, x: int, y: int) -> None:
        if self.visibleStamps.get((x, y), None) is None:
            return
        stamp, sid = self.visibleStamps.pop((x, y))
        stamp.clearstamp(sid)

    def erase_all(self) -> None:
        for stamp, sid in self.visibleStamps.values():
            stamp.clearstamp(sid)
        self.visibleStamps = dict()

    def update(self) -> None:
        self.screen.update()

    def _draw_entity(self, entity: Turtle, x: int, y: int) -> None:
        px = self.CELL_SIZE * x
        py = self.CELL_SIZE * y
        entity.setposition(px, py)
        if self.visibleStamps.get((x, y), None) is not None:
            self.erase(x, y)

        self.visibleStamps[(x, y)] = (entity, entity.stamp())

    def _draw_arena(self, pwidth: int, pheight: int) -> None:
        x0 = -self.CELL_SIZE / 2
        y0 = -self.CELL_SIZE / 2

        drawer: Turtle = _make_turtle("blue")
        drawer.begin_fill()
        drawer.setposition(x0, y0)
        drawer.setposition(x0 + pwidth, y0)
        drawer.setposition(x0 + pwidth, y0 + pheight)
        drawer.setposition(x0, y0 + pheight)
        drawer.setposition(x0, y0)
        drawer.end_fill()

class TurtlePathVisualiser(PathVisualiser):
    PATH_WIDTH: int = 2

    ui: TurtleUI
    paths: dict[id, Turtle]
    lastPid: int

    def __init__(self, ui: TurtleUI) -> None:
        self.ui = ui
        self.paths = dict()
        self.lastPid = -1

    def draw_path(self, points: list[Point], colour: str) -> int:
        pid = self._new_pid()
        drawer = _make_turtle(colour)

        drawer.width(self.PATH_WIDTH)
        drawer.setposition(*points[0])
        drawer.pendown()
        for point in points[1:]:
            drawer.setposition(point.x * self.ui.CELL_SIZE, point.y * self.ui.CELL_SIZE)
        drawer.penup()

        self.paths[pid] = drawer
        return pid

    def erase(self, pid, int) -> None:
        if drawer := self.paths.get(pid, None) is None:
            return
        drawer.clear()
        self.paths.pop(pid)

    def erase_all(self) -> None:
        for drawer in self.paths.items():
            drawer.clear()
        self.paths = dict()

    def update(self) -> None:
        self.ui.update() # kinda bad... breaks seperation between ui and visualiser

    def _new_pid(self) -> int:
        self.lastPid += 1
        return self.lastPid
