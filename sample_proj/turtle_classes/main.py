from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_input = screen.textinput(title='AAA' , prompt='Guess color').lower()

color = ['blue', 'green', 'yellow', 'orange', 'red', 'purple','brown']
random.shuffle(color)

turtles = []
for i in range(0,len(color)):
    t = Turtle(shape='turtle')
    t.color(color[i])
    t.penup()
    t.goto(x=-240 ,y=(120 - 40 * i))
    turtles.append(t)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f'You have win with the {user_input} turtle')
            else:
                print(f'Your {user_input} turtle has lost')

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()