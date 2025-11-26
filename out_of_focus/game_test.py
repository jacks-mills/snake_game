from snake import Snake
from point import Point
from game import Game

def game_invariant_available_apple_spaces_and_snake_segments_union(game: Game) -> None:
    allPoints = {Point(x, y) for x in range(game.width) for y in range(game.height)}
    missing = allPoints - (game.availableAppleSpaces | set(game.snake.segments))
    condition = missing == set()
    err = (f"Intersection between game.availeAppleSpaces and game.snake.segments "
           f"does not cover all points. Missing {list(missing)[:10]}")
    assert condition, err

def game_invariant_available_apple_spaces_and_snake_segments_intersection(game: Game) -> None:
    condition = game.availableAppleSpaces & set(game.snake.segments) == set()
    err = (f"Non empty intersection between game.availeAppleSpaces and game.snake.segments: "
           f"{game.availableAppleSpaces & set(game.snake.segments)}")
    assert condition, err

def game_invariant_snake_in_bound(game: Game) -> None:
    condition = (0 <= game.snake.head.x <= game.width and 0 <= game.snake.head.y <= game.height)
    err = f"Snake out of bounds: {game.snake.head}"
    assert condition, err

def game_invariants(game) -> None:
    game_invariant_available_apple_spaces_and_snake_segments_union(game)
    game_invariant_available_apple_spaces_and_snake_segments_intersection(game)
    game_invariant_snake_in_bound(game)
