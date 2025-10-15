from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.win_score = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.left_score, align= "center", font = ("Comic Sans MS", 20, "normal"))
        self.goto(100, 210)
        self.write(self.right_score, align= "center", font = ("Comic Sans MS", 20, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def check_winner(self):
        if self.left_score >= self.win_score:
            return "Left"
        elif self.right_score >= self.win_score:
            return "Right"
        return None

    def display_winner(self, winner):
        self.goto(0,0)
        self.write(f"{winner} Player Wins!", align="center", font=("Comic Sans MS", 40, "bold"))

    def show_start_message(self):
        self.goto(0, 0)
        self.write("Press SPACE to Start", align="center", font=("Comic Sans MS", 30, "bold"))

    def clear_start_message(self):
        self.clear()
        self.update_scoreboard()