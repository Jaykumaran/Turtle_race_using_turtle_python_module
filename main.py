
from turtle import Turtle,Screen
import random

colors=["red","green","yellow","orange","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]

all_turtle=[]
screen=Screen()
screen.setup(width=500, height= 400)
is_race_on=False

user_bet=screen.textinput(title="Make your bet",prompt="Which colored turtle will win race: ")
for turtle_index in range(0,6):

 new_turtle=Turtle(shape="turtle")
 new_turtle.penup()
 new_turtle.goto(x=-240, y=y_positions[turtle_index])
 new_turtle.color(colors[turtle_index])
 all_turtle.append(new_turtle)


if user_bet:
    is_race_on=True
while is_race_on:
    for turtle_item in all_turtle:
        if turtle_item.xcor()>230:
            is_race_on=False
            win_color_turtle=turtle_item.pencolor()
            if win_color_turtle==user_bet:
                print(f"you won,Winning turtle is {win_color_turtle} color.")
            else:
                print(f"you lost,Winning turtle is {win_color_turtle} color.")
        random_distance= random.randint(0,10)
        turtle_item.forward((random_distance))





screen.exitonclick()