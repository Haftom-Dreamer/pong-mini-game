from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,n,b):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(n,b)
        self.color("white")
        self.update
    
    def update(self):
        self.write(arg = (f"{self.score}"), align="center", font =("Arial", 50, "normal"))

    def display(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self, n):
        self.goto(0,0)
        self.write(arg = f"GAME OVER\n{n} won" , align="center", font =("Arial", 17, "normal"))
    def line (self):
        self.write(arg =   
"""
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
""" , align="center", font =("Arial", 17, "normal"))
