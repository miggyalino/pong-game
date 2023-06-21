from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.difficulty = 0.0125
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(100,250)
        self.write(f"{self.right_score}",align="center",font=("Arial",34,"bold"))
        self.goto(-100,250)
        self.write(f"{self.left_score}",align="center",font=("Arial",34,"bold"))
    
    def update_right(self):
        self.right_score += 1
        self.clear()
        self.goto(-100,250)
        self.write(f"{self.left_score}",align="center",font=("Arial",34,"bold"))
        self.goto(100,250)
        self.write(f"{self.right_score}",align="center",font=("Arial",34,"bold"))
        
    def update_left(self):
        self.left_score += 1
        self.clear()
        self.goto(-100,250)
        self.write(f"{self.left_score}",align="center",font=("Arial",34,"bold"))
        self.goto(100,250)
        self.write(f"{self.right_score}",align="center",font=("Arial",34,"bold"))

    def update_difficulty(self):
        if self.right_score == 2 or self.left_score == 2:
            self.difficulty *= 0.9
        if self.right_score == 4 or self.left_score == 4:
            self.difficulty *= 0.9
        if self.right_score == 6 or self.left_score == 6:
            self.difficulty *= 0.9
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align="center",font=("Arial",26,"bold"))
        
        