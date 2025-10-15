from turtle import Turtle

move_distance = 20
top_boundary = 240
bottom_boundary = -240


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.starting_position = position


    def go_up(self):
        new_y = min(self.ycor() + move_distance, top_boundary)
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = max(self.ycor() - move_distance, bottom_boundary)
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(self.starting_position)

