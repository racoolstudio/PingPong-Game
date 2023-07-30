# Import the Turtle module to create a Ball class that represents the game ball.

from turtle import Turtle


# Define the Ball class that inherits from Turtle.
class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Turtle).
        self.create()  # Create the ball with its initial properties.
        self.x_move = 10  # Set the initial horizontal movement of the ball.
        self.y_move = 10  # Set the initial vertical movement of the ball.
        self.ball_speed = 0.08  # Set the initial speed of the ball.

    # Method to move the ball according to its x_move and y_move values.
    def move(self):
        new_x = self.xcor() + self.x_move  # Calculate the new x-coordinate for the ball.
        new_y = self.ycor() + self.y_move  # Calculate the new y-coordinate for the ball.
        self.goto(new_x, new_y)  # Move the ball to the new position.

    # Method to make the ball bounce off the top and bottom walls.
    def wall_bounce(self):
        self.y_move *= -1  # Reverse the vertical movement direction of the ball.

    # Method to make the ball bounce off the paddles.
    def paddle_bounce(self):
        self.x_move *= -1  # Reverse the horizontal movement direction of the ball.
        self.ball_speed *= 0.9  # Increase the ball's speed to increase difficulty.

    # Method to create the initial properties of the ball.
    def create(self):
        self.penup()  # Penup to prevent drawing lines when moving the ball.
        self.shape('circle')  # Set the shape of the ball to a circle.
        self.color('white')  # Set the color of the ball to white.
        self.shapesize(1, 1)  # Set the size of the ball.
        self.goto(0, 0)  # Position the ball at the center of the screen.

    # Method to update the ball's position, speed, and direction when a point is scored.
    def update(self):
        self.goto(0, 0)  # Move the ball back to the center.
        self.ball_speed = 0.08  # Reset the ball's speed to its initial value.
        self.paddle_bounce()  # Reverse the ball's direction after scoring a point.
