from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard



screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

f_paddle = Paddle(-350)
f_paddle2 = Paddle(350)
ball = Ball()
score_1 = ScoreBoard(100, 230)
score_2 = ScoreBoard(-100, 230)
score = ScoreBoard(0, -320) 
score.line()
score_1.update()
score_2.update()



screen.onkey(f_paddle.up, "w")
screen.onkey(f_paddle.down, "s")
screen.onkey(f_paddle2.up, "o")
screen.onkey(f_paddle2.down, "l")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_b()
    if ball.distance(f_paddle2) < 50 and ball.xcor() > 320  or ball.distance(f_paddle) < 50 and ball.ycor() > -320 :
        ball.bounce_p()
    if ball.xcor() > 390:
        score_2.display()
        ball.goto(0,0)
        ball.bounce_p()
    if ball.xcor() < -390:
        score_1.display()
        ball.goto(0,0)
        ball.bounce_p()
    if score_1.score > 4:
       game_on = False
       score_1.game_over("player two")
    if score_2.score > 4:
       score_2.game_over("player one")
       game_on = False
     

    







screen.exitonclick()