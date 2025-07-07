from turtle import Turtle
FONT = ("Courier", 64, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color('white')
        self.player_score = 0
        self.bot_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_score,align= 'center', font= FONT )
        self.goto(100, 200)
        self.write(self.bot_score,align= 'center', font= FONT )

    def player_point(self):
        self.player_score += 1
        self.update_scoreboard()
    def bot_point(self):
        self.bot_score += 1
        self.update_scoreboard()