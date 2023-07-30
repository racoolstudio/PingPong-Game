# Import the Turtle module to create a Score class that will handle the game score display.

from turtle import Turtle


# Define the Score class that inherits from Turtle.
class Score(Turtle):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Turtle).
        self.penup()  # Penup to prevent drawing lines between score updates.
        self.hideturtle()  # Hide the turtle icon from the screen.
        self.score_right = 0  # Initialize the score for the right player to 0.
        self.score_left = 0  # Initialize the score for the left player to 0.
        self.goto(0, 260)  # Set the initial position for the score display.
        self.color('white')  # Set the color of the text to white.
        self.write(f'{self.score_left}  {self.score_right}', False, 'center',
                   ('verdana', 40, 'bold'))  # Display the initial score.

    # Method to update the score display on the screen.
    def write_score(self):
        self.clear()  # Clear the previous score display.
        self.write(f'{self.score_left}   {self.score_right}', False, 'center',
                   ('Verdana', 40, 'bold'))  # Write the updated score.

    # Method to update the score for the right player and update the score display.
    def update_right(self):
        self.score_right += 1  # Increment the score for the right player by 1.
        self.write_score()  # Update the score display with the new score.

    # Method to update the score for the left player and update the score display.
    def update_left(self):
        self.score_left += 1  # Increment the score for the left player by 1.
        self.write_score()  # Update the score display with the new score.
