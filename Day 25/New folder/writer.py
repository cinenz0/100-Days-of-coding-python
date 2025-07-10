from turtle import Turtle

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color('black')
        self.x = 0
        self.y = 0

    def write_state(self, word):
        self.goto(self.x,self.y)
        self.write(f'{word}')