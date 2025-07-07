from turtle import Turtle
SPEED_INCREASE = 0.5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.pu()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1      
    def bounce_y(self):
        self.y_move *= -1

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()

    def speed_up(self):
        if self.x_move < 0:
            self.x_move -= SPEED_INCREASE

        if self.y_move < 0: 
            self.y_move -= SPEED_INCREASE

        if self.x_move > 0: 
            self.x_move += SPEED_INCREASE

        if self.y_move > 0:
            self.y_move += SPEED_INCREASE

    def reset_speed (self):
        if self.x_move < 0:
            self.x_move = -10

        if self.y_move < 0: 
            self.y_move = -10

        if self.x_move > 0: 
            self.x_move = 10

        if self.y_move > 0:
            self.y_move = 10