from turtle_ui import TurtleUI
from typing import NamedTuple
from ui import UI

class Config(NamedTuple):
    # board dimensions
    width: int
    height: int

    # key bindings
    resetKey: str
    quitKey: str
    pauseKey: str
    upKey: str
    downKey: str
    leftKey: str
    rightKey: str

    # frame rate
    millisecondsPerFrame: int

CONFIG = Config(
        width = 5,
        height = 5,

        resetKey = "r",
        quitKey = "q",
        pauseKey = "space",
        upKey = "Up",
        downKey = "Down",
        leftKey = "Left",
        rightKey = "Right",

        millisecondsPerFrame = 500)

