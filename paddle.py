from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xcor):
        super().__init__()
        self.color("white")  
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(xcor, 0)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y =self.ycor() - 20
        self.goto(self.xcor(), new_y)
