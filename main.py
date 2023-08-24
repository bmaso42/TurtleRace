from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="Step right up!", prompt="Which color turtle do you think will win?")

colors = ["red", "yellow", "orange", "blue", "purple"]
y_position = [-120, -60, 0, 60, 120]
turtles = []

for turtle_index in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.setpos(x=-230, y=y_position[turtle_index])
    # tim.pendown()
    turtles.append(tim)

def race():
    running = True
    while running:
        for x in range(0, 5):
            turtles[x].forward(random.randrange(5, 25))
            if turtles[x].xcor() >= 225:
                running = False
                screen.bye()
                return turtles[x].color()


winner = race()
if winner[0] == guess:
    print("Your turtle won the race!")
else:
    print(f"You lose! The winning turtle was {winner[0]}.")


# screen.exitonclick()