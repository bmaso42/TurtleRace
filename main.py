from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
# guess = screen.textinput(title="Step right up!", prompt="Which color turtle do you think will win?")

colors = ["red", "yellow", "orange", "blue", "purple"]
y_position = [-120, -60, 0, 60, 120]

for turtle_index in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.setpos(x=-230, y=y_position[turtle_index])
    tim.pendown()



screen.exitonclick()