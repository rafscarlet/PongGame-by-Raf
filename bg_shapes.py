from turtle import Turtle


class Timmy(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("green")
        self.speed("fast")
    
    def draw_line(self):
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)
        self.penup()
        self.home()
    
    def draw_circle(self):
        self.goto(0, -60)
        self.setheading(0)
        self.pendown()
        self.circle(60)
