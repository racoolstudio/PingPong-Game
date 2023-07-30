# Import the necessary modules and classes to set up the Pong game.

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import Score

# Create the game screen.
my_screen = Screen()
my_screen.title('PONG')
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.tracer(0)

# Create paddles and ball objects.
paddle_1 = Paddle(x=350, y=0)
paddle_2 = Paddle(x=-350, y=0)
ball = Ball()
scoreBoard = Score()

# Set up key events for paddle movements.
my_screen.listen()
my_screen.onkey(paddle_1.move_up, 'Up')
my_screen.onkey(paddle_1.move_down, 'Down')
my_screen.onkey(paddle_2.move_up, 'w')
my_screen.onkey(paddle_2.move_down, 's')
my_screen.onkey(paddle_2.move_up, 'W')
my_screen.onkey(paddle_2.move_down, 'S')

# Variable to control the game loop.
isOn = True

# Draw the center line.
line = Turtle()
line.penup()
line.color('white')
line.hideturtle()
line.goto(0, 270)


def draw_line():
    for i in range(270, -300, -20):
        line.write(':', False, 'center', ('verdana', 30, 'bold'))
        line.write('', False, 'center', ('verdana', 30, 'bold'))
        line.goto(0, i)


draw_line()

# Game loop
while isOn:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()

    # Check for wall collisions
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    # Check for paddle collisions
    if (ball.xcor() >= 320 and (ball.distance(paddle_1) <= 50 or ball.distance(paddle_1) <= 60)) or (
            ball.xcor() <= -320 and (ball.distance(paddle_2) <= 50 or ball.distance(paddle_2) <= 70)):
        ball.paddle_bounce()

    # Check for scoring on each side and update the score accordingly
    if ball.xcor() >= 380:
        scoreBoard.update_left()
        ball.update()
    elif ball.xcor() <= -370:
        scoreBoard.update_right()
        ball.update()

# Close the game window when clicked.
my_screen.exitonclick()
