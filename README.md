## How the game works
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
3. When the turtle reaches at the other end, you pass the level and +1 in your scoreboard
4. Each level passes, the car's movement speed

## Steps on how I make this game
A few things that are required in this game are:
* Step 1: Move the turtle with keypress
  * Create a screen of your game with selected width and height. This will be used to determine your starting and finishing line
  * Create turtle as "player"
  * Assign keypress using screen.onkey()
* Step 2: Create and move cars horizontally
  * Create cars with random y-coordinate generated
  * Lengthen the shape to make it as "car"
* Step 3: Detect the collision with car
  * Ends the game without exiting the screen using screen.exitonclick()
* Step 4: Detect turtle when reaching the other side
  * Increase difficulty by increasing the car_speed
* Step 5: Create scoreboard
  * Shows the current level of the game
  * Shows "Game Over"


###### Remark:
1. My code doesn't work when I assign a variable named "car" with class Car (raises AttributeError where it called on class Turtle instead Car) but it works when I use other name than "car" such as "vehicle" or "bus" and I donno why :/
2. I created this game in Pycharm
