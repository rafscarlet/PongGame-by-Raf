from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.color("white")
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)

        