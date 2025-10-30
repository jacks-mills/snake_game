# Plan

Table of Contents
* What Data is Needed
* How Data Will Change
* Types of Data Queries
* Game loop
* Snake agent strategies






## What Data is Needed
* configuration

* snake segment positions (head and body)
* snake heading
* apple position
* play area dimensions (and shape...?)

* game state (menu, playing, won, lost, quit)
* last movement input (before step)
* ui state (whats displayed)




## How Data Will Change
Immutable data
* configuraiton
* play area dimensions (might be changable in future)

Snake segments
* movement: positions change when snake moves
* growth: segment added when snake grows

Apple position
* position changes after snake east apple, replace with apple in empty cell

Game State
* Player starts game    user input: menu -> playing
* Player quits game     user input: menu, won, lost, playing -> quit
* Player restarts game  user input: won, lost, playing -> menu/playing (undecided)
* Player wins game      game play: playing -> won
* Player loses game     game play: playing -> lost

UI
* game data (snake segment positions, apple position) change

Last Movement Input
* user input



## Types of Data Queries
configuration
* what value does each configuration option have

Snake
* Position of segments
* Position of head
* Is head colliding with body
* Is the snake in bounds
* Is the snake eating an apple

Apple
* Position of apple

Dimensions
* what are the dimensions



## Game loop:
* get input (should think of types of inputs other than snake movements, e.g. quit, restart, ...)
* update snake
* update state
* update ui

* NOTE: treat whole game as encapsulated thing, outside caller steps through game and 

    * state updates
    * snake movement: move snake in direction of head heading
    * snake growth/eating: check if snake ate apple, if so grow snake
    * apple placement: after snake eats apple, find place for new apple

    * state queries
    * snake collision: has the snake collided with itself of the screen edge
    * game won: is board full of snake


## Snake Agent Strategy
* hamiltonian path: path that goes through each point, snake cannot die, collide with itself or the
  walls, if on this path

* snake path: my idea, snake cannot die if it is travelling in a loop that is at least as long as
  the snake (or one longer, for the case where it eats an apple). Loop idea came to me after
  watching this snake game: https://www.youtube.com/watch?v=1fkV5rB13jQ

* Consider how the space taken up by the snake body determines where the apple can spawn, and that
  more clear space near the snakes head gives a higher chance the apple will spawn near the snake's
  head
