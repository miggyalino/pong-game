from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

rPaddle = Paddle((350,0))
lPaddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(rPaddle.go_up, "Up")
screen.onkeypress(rPaddle.go_down, "Down")
screen.onkeypress(lPaddle.go_up, "w")
screen.onkeypress(lPaddle.go_down, "s")

gameOn = True
while gameOn:
    time.sleep(scoreboard.difficulty)
    screen.update()
    ball.move()
    #Detect Collision with upper and lower wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounceY()


    if (rPaddle.distance(ball) < 50 and ball.xcor() > 320 and ball.moveX > 0) or (lPaddle.distance(ball) < 50 and ball.xcor() < -320 and ball.moveX < 0):
        ball.bounceX()
       
    if ball.xcor() == 390:
        scoreboard.update_left()
        scoreboard.update_difficulty()
        ball.goto(0,0)
        time.sleep(1)
        ball.moveX = -5
        time.sleep(scoreboard.difficulty)
        ball.move()
    elif ball.xcor() == -390:
        scoreboard.update_right()
        scoreboard.update_difficulty()
        ball.goto(0,0)
        time.sleep(1)
        ball.moveX = 5
        time.sleep(scoreboard.difficulty)
        ball.move()

    if scoreboard.left_score == 7 or scoreboard.right_score == 7:
        scoreboard.game_over()
        gameOn = False
        
            


screen.exitonclick()

