from turtle import Screen, Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self, starting_length = 3):
        self.starting_length = starting_length
        self.segments = []
        for _ in STARTING_POSITIONS:
            square = self.create_segment(_)
            self.segments.append(square)
        self.head = self.segments[0]

    
    def create_segment(self, position):
        square = Turtle(shape = 'square')
        square.pu()
        square.color('white')
        square.goto(position)
        return square

    def move(self):
        for segment in range(len(self.segments)-1,0,-1):  
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x = new_x, y= new_y)
        self.segments[0].fd(MOVE_DISTANCE)
    
    def add_segment(self):
        self.segments.append(self.create_segment(self.segments[-1].position()))
    
    def up(self):
    
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
       
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
