from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos = (-350, 0)):
        super().__init__()
        self.pos = pos
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid = 5,stretch_len = 1)
        self.pu()
        self.goto(self.pos)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(),y= new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x = self.xcor(),y= new_y)