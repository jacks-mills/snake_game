from turtle_ui import TurtleUI
from typing import NamedTuple
from ui import UI

class Config(NamedTuple):
    ui: UI
    width: int
    height: int

WIDTH = 10
HEIGHT = 10
CONFIG = Config(TurtleUI(WIDTH, HEIGHT), WIDTH, HEIGHT)
