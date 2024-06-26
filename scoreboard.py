from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self, position):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.score = 0
        self.position = position
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(self.position)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))
        