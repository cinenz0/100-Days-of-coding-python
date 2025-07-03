from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? ")
colors = ['red','orange','yellow','green','blue','purple']
y_plus = -70
turtles_list = []
for color in colors:
    tim = Turtle(shape='turtle')
    tim.color(color)
    tim.pu()
    tim.goto(x=-230,y=y_plus)
    y_plus += 30 
    turtles_list.append(tim)

winning_color = ''
while True:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor() 
        turtle.fd(random.randint(0, 10))
    if winning_color:
        break
if winning_color == user_bet:
    print(f"You'be won! The {winning_color} turtle has won the race")  
else:
    print(f"You'be lost! The {winning_color} turtle has won the race")
               
screen.exitonclick()