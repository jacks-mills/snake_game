from player_controller import PlayerController
from boardstate import BoardState
from turtle_ui import TurtleUI

def main():
    WIDTH = 10
    HEIGHT = 10
    MILLISECONDS_PER_FRAME = 250

    board = BoardState(WIDTH, HEIGHT)
    ui = TurtleUI(WIDTH, HEIGHT)

    controller = PlayerController(ui, board, MILLISECONDS_PER_FRAME)

    ui.screen.mainloop()

        



if __name__ == "__main__":
    main()
