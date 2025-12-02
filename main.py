from player_controller import PlayerController
from config import CONFIG

def main():
    controller = PlayerController(CONFIG)
    controller.mainloop()


if __name__ == "__main__":
    main()
