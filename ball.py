from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.movement_speed *= 0.8

    def restart(self):
        self.goto(0,0)
        self.movement_speed = 0.1
        self.x_bounce()


