from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALIGN = 'center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.score = 0
        self.goto(0, 256)
        self.change_score()
        self.hideturtle()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align = ALIGN, font = FONT )

    def change_score(self):
        self.clear()
        self.write(f'Score: {self.score}',align = ALIGN, font = FONT )
        