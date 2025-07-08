from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.pu()
        self.turtlesize(stretch_wid = 1,stretch_len = 2)
        self.color(random.choice(COLORS))
        self.goto(280, random.randint(-240, 280))
        self.setheading(180)
        self.level = 0


    def auto_move(self):
        if self.xcor() > -320:
            self.fd(STARTING_MOVE_DISTANCE + self.increment_speed())

    def increment_speed (self):
        return self.level * MOVE_INCREMENT
        
