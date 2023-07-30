# Import the Turtle module to create a Paddle class that represents a player's paddle.

from turtle import Turtle

# Set the paddle movement distance.
DISTANCE = 60


# Define the Paddle class that inherits from Turtle.
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()  # Call the constructor of the parent class (Turtle).
        self.penup()  # Penup to prevent drawing lines when moving the paddle.
        self.shape('square')  # Set the shape of the paddle to a square.
        self.color('white')  # Set the color of the paddle to white.
        self.shapesize(stretch_wid=1, stretch_len=5)  # Stretch the square to form a paddle.
        self.x = x  # Set the initial x-coordinate for the paddle.
        self.y = y  # Set the initial y-coordinate for the paddle.
        self.goto(x=self.x, y=self.y)  # Position the paddle at the specified coordinates.
        self.right(90)  # Rotate the paddle 90 degrees to face upwards.

    # Method to move the paddle down by the defined distance.
    def move_down(self):
        self.forward(DISTANCE)

    # Method to move the paddle up by the defined distance.
    def move_up(self):
        self.back(DISTANCE)
