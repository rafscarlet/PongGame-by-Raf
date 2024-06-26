import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bg_shapes import Timmy

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong - The first game (remade by Raf)")
screen.bgcolor("black")
timmy = Timmy()
timmy.draw_line()
timmy.draw_circle()
screen.tracer(0)

paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))

ball = Ball()
score_left = Scoreboard((-100, 200))
score_right = Scoreboard((100, 200))

# Move paddles
screen.listen()
# Paddle 1 (left)
screen.onkey(fun=paddle_1.move_up, key="w")
screen.onkey(fun=paddle_1.move_down, key="s")
# Paddle 2(right)
screen.onkey(fun=paddle_2.move_up, key="Up")
screen.onkey(fun=paddle_2.move_down, key="Down")

screen_on = True
while screen_on:
    time.sleep(ball.sleep_time)
    ball.move()
    screen.update()
    
    # Detect collision with upper or lower wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    
    # Detect collision with paddles
    if (ball.xcor() > 330 and ball.distance(paddle_2) < 55) or (ball.xcor() < -330 and ball.distance(paddle_1) < 50):
        ball.bounce_x()
        ball.incr_speed()
    
    # Out of bounds (right side)
    if ball.xcor() > 350:
        ball.reset_position()
        score_left.score += 1
        score_left.write_score()
    # Out of bounds (left side)
    if ball.xcor() < -350:
        ball.reset_position()
        score_right.score += 1
        score_right.write_score()
    

screen.exitonclick()
