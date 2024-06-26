from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1
        
    def incr_speed(self):
        self.sleep_time *= 0.9
        
    def move(self):
        # Move the ball
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.home()
        self.sleep_time = 0.1
        self.bounce_x()
        