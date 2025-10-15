import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score

The_screen = Screen()
The_screen.setup(width=800, height=600)
The_screen.bgcolor("white")
The_screen.title("WELCOME TO PONG LAND")

The_screen.tracer(0)

right_Paddle = Paddle((350, 0))
left_Paddle = Paddle((-350, 0))

score = Score()
ball = Ball()

score.show_start_message()

game_started = False

def start_game():
    global game_started
    if not game_started:
        game_started = True
        score.clear_start_message()

The_screen.listen()
The_screen.onkey(start_game, "space")
The_screen.onkeypress(left_Paddle.go_up, "w")
The_screen.onkeypress(left_Paddle.go_down, "s")
The_screen.onkeypress(right_Paddle.go_up, "Up")
The_screen.onkeypress(right_Paddle.go_down, "Down")

game_on = True
while game_on:
    The_screen.update()

    if game_started:
        time.sleep(ball.movement_speed)
        ball.move()


        #detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        #detect collision with right paddle
        if (ball.distance(right_Paddle) < 60 and ball.xcor() > 320 or
        ball.distance(left_Paddle) < 60 and ball.xcor() < -320):
            ball.x_bounce()

        #detect when right paddle misses
        if ball.xcor() > 360:
            ball.restart()
            score.left_point()
            left_Paddle.reset_position()
            right_Paddle.reset_position()

        #detect when left paddle misses
        if ball.xcor() < -360:
            ball.restart()
            score.right_point()
            left_Paddle.reset_position()
            right_Paddle.reset_position()

        #detect when someone wins
        winner = score.check_winner()
        if winner:
            score.display_winner(winner)
            game_on = False

The_screen.exitonclick()
