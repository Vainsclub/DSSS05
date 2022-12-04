import turtle
import numpy as np
import random


def main(speed=0, bg_color="grey"):

    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()

    myTurtle.speed(speed)

    turtle_screen.bgcolor(bg_color)
    colours = ["cyan", "purple", "blue", "red","green"]
    """TODO: define different colors here"""


    for _ in range(10):

        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]
        myTurtle.color(random.choice(colours))



        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()


        for _ in range(8):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)


def snowflake_branch(size, myTurtle):

    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
