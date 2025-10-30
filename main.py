from game import Game, update_ui
from config import CONFIG

from snake import Heading
from turtle_ui import TurtlePathVisualiser
from point import Point



def main():

    game: Game = Game(CONFIG.width, CONFIG.height)

    ui = CONFIG.ui
    visualiser = TurtlePathVisualiser(ui)

    visualiser.draw_path([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1), Point(0, 0)], "green")
    visualiser.update()

    def on_key(event):
        match event.keysym:
            case "Up":
                game.set_new_heading(Heading.NORTH)
            case "Down":
                game.set_new_heading(Heading.SOUTH)
            case "Left":
                game.set_new_heading(Heading.WEST)
            case "Right":
                game.set_new_heading(Heading.EAST)
    
    root = ui.screen.getcanvas().winfo_toplevel()
    root.bind("<Key>", on_key)

    def loop():
        game.step()
        update_ui(ui, game)
        ui.screen.ontimer(loop, 250)

    loop()

    input()
        



if __name__ == "__main__":
    main()
