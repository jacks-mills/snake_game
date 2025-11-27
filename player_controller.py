from boardstate import BoardState
from turtle_ui import TurtleUI
from ui import UI
from snake import Snake, Heading

class PlayerController:
    ui: TurtleUI
    board: BoardState
    millisecondsPerStep: int

    newHeading: Heading | None
    started: bool

    def __init__(self, ui: TurtleUI, board: BoardState, millisecondsPerStep: int) -> None:
        self.ui = ui
        self.board = board
        self.millisecondsPerStep = millisecondsPerStep

        self.newHeading = None
        self.started = False

        update_ui(self.ui, self.board)

        self.ui.screen.onkeypress(self.up, "Up")
        self.ui.screen.onkeypress(self.down, "Down")
        self.ui.screen.onkeypress(self.left, "Left")
        self.ui.screen.onkeypress(self.right, "Right")

        self.ui.screen.onkeypress(self.quit, "q")
        self.ui.screen.onkeypress(self.reset, "r")
        self.ui.screen.listen()

    def up(self) -> None:
        self._move(Heading.NORTH)

    def down(self) -> None:
        self._move(Heading.SOUTH)

    def left(self) -> None:
        self._move(Heading.WEST)

    def right(self) -> None:
        self._move(Heading.EAST)

    def quit(self) -> None:
        self.ui.screen.bye()

    def reset(self) -> None:

    def _move(self, heading: Heading) -> None:
        self.newHeading = heading
        if self.started == False:
            self.started = True
            self.board.snake._heading = heading
            self.newHeading = None
            self.step()

    def step(self) -> None:
        self.board.step(self.newHeading)
        self.newHeading = None
        update_ui(self.ui, self.board)
        self._schedule_step()

    def _schedule_step(self) -> None:
        self.ui.screen.ontimer(self.step, self.millisecondsPerStep)


def update_ui(ui: UI, board: BoardState) -> None:
    ui.erase_all()

    for body in board.snake.segments[1:]:
        ui.draw_snake_body(*body)
    ui.draw_snake_head(*board.snake.head)

    if board.apple is not None:
        ui.draw_apple(*board.apple)
