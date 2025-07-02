import colorgram
from turtle import Turtle, Screen
import turtle as turtle_module
import random

def main():
    t = Turtle()
    turtle_module.colormode(255)
    t.speed(20)
    t.pu()
    position(t)
    t.hideturtle()
    dots_per_line = 10
    lines = 10
    for _ in range(lines):
        make_dot(t, dots_per_line)
        new_line(t)
def position(t):
    t.setheading(225)
    t.fd(300)
    t.setheading(0)

def make_dot(t, dotspl):
    colors = colorgram.extract('image.jpg', 30 )
    rgb_colors = []
    [rgb_colors.append(tuple(color.rgb)) for color in colors]
    for _ in range(dotspl):
        t.dot(20, random.choice(rgb_colors))
        t.fd(50)
    
def new_line (t):
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(500)
    t.setheading(0)

main()