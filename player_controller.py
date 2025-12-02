from board import Board, BoardState, Heading
from turtle_ui import TurtleUI
from ui import UI
from config import Config
from enum import Enum
import time

class ControllerState(Enum):
    RESET = 1
    PAUSED = 2
    PLAYING = 3
    FINISHED = 4

class PlayerController:
    config: Config

    ui: TurtleUI
    board: Board
    state: ControllerState

    stepScheduledTime: int

    def __init__(self, config: Config) -> None:
        self.config = config

        self.ui = TurtleUI(config.width, config.height)

        self.ui.screen.onkeypress(self.reset, self.config.resetKey)
        self.ui.screen.onkeypress(self.quit, self.config.quitKey)
        self.ui.screen.onkeypress(self.pause, self.config.pauseKey)
        self.ui.screen.onkeypress(self.up, self.config.upKey)
        self.ui.screen.onkeypress(self.down, self.config.downKey)
        self.ui.screen.onkeypress(self.left, self.config.leftKey)
        self.ui.screen.onkeypress(self.right, self.config.rightKey)
        self.ui.screen.listen()

        self.reset()

    def mainloop(self) -> None:
        self.ui.screen.mainloop()

    def reset(self) -> None:
        self.board = Board(self.config.width, self.config.height)
        self.state = ControllerState.RESET
        self.stepScheduledTime = 0
        update_ui(self.ui, self.board)

    def quit(self) -> None:
        self.ui.screen.bye()

    def pause(self) -> None:
        if self.state in [ControllerState.RESET, ControllerState.FINISHED]:
            return

        if self.state == ControllerState.PAUSED:
            self.state = ControllerState.PLAYING
            self.schedule_step()
            return
        
        if self.state == ControllerState.PLAYING:
            self.state = ControllerState.PAUSED
            return


    def up(self) -> None:
        self.move(Heading.NORTH)

    def down(self) -> None:
        self.move(Heading.SOUTH)

    def left(self) -> None:
        self.move(Heading.WEST)

    def right(self) -> None:
        self.move(Heading.EAST)

    def move(self, heading: Heading) -> None:
        if self.state == ControllerState.RESET:
            self.state = ControllerState.PLAYING
            self.board.set_new_heading(None)
            self.board.heading = heading
            self.step()
            return

        if self.state == ControllerState.PLAYING:
            self.board.set_new_heading(heading)
            return

    def step(self) -> None:
        if self.state != ControllerState.PLAYING:
            return

        if self.stepScheduledTime > time_ms():
            return

        self.board.step()
        update_ui(self.ui, self.board)

        if self.board.state == BoardState.PLAYING:
            self.schedule_step()
            return
        
        self.state = ControllerState.FINISHED
        if self.board.state == BoardState.GAME_WON:
            print("Game won!")
        elif self.board.state == BoardState.GAME_OVER:
            print("Game over!")
        return

    def schedule_step(self) -> None:
        self.stepScheduledTime = time_ms() + self.config.millisecondsPerFrame
        self.ui.screen.ontimer(self.step, self.config.millisecondsPerFrame)


def time_ms():
    return time.time_ns() // 1000000

def update_ui(ui: UI, board: Board) -> None:
    ui.erase_all()

    ui.draw_snake_head(*board.snake[0])
    for body in board.snake[1:]:
        ui.draw_snake_body(*body)

    if board.fruit is not None:
        ui.draw_fruit(*board.fruit)
