from turtle import Screen
from player import Player
import random
import time
from ball import Ball
from scoreboard import Scoreboard
from divider import Divider

screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player_l = Player((-350, 0))
player_r = Player((350, 0))
ball = Ball()
score = Scoreboard()
divider = Divider()

screen.listen()
screen.onkey(player_l.up, "Up")
screen.onkey(player_l.down, "Down")
screen.onkey(player_r.up, "w")
screen.onkey(player_r.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    ball.move()

    #detect the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect the right paddle:
    if ball.distance(player_r) < 50 and ball.xcor() > 330 or ball.distance(player_l) < 50 and ball.xcor() < -330:
        ball.bounce_p()

    if ball.xcor() > 400:
        score.increase_score_l()
        ball.refresh()
    elif ball.xcor() < -400:
        score.increase_score_r()
        ball.refresh()


    









screen.exitonclick()