from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self, ) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.moveX = 5
        self.moveY = 5
    
    def move(self):
        x = self.xcor() + self.moveX
        y = self.ycor() + self.moveY
        self.goto(x,y)

    def bounceY(self):
        self.moveY *= -1

    def bounceX(self):
        self.moveX *= -1