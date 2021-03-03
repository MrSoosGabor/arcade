import turtle
import time
import random


def fel():
    y = ship.ycor() + 20
    if y > 280:
        ship.sety(-280)
    else:
        ship.sety(y)


def le():
    y = ship.ycor() - 20
    if y < -280:
        ship.sety(280)
    else:
        ship.sety(y)


def jobbra():
    x = ship.xcor() + 20
    if x > 380:
        ship.setx(-380)
    else:
        ship.setx(x)


def balra():
    x = ship.xcor() - 20
    if x < -380:
        ship.setx(380)
    else:
        ship.setx(x)


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("space.png")
space.addshape("sprite.gif")
space.addshape("meteor1.gif")
space.addshape("meteor2.gif")
space.addshape("meteora.gif")
space.tracer(0)

space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(jobbra, "Right")
space.onkeypress(balra, "Left")
space.listen()

ship = turtle.Turtle()
ship.shape("sprite.gif")

meteorok = []


def uj_meteor():
    meteor = turtle.Turtle()
    meteor.shape("meteor2.gif")
    y = random.randint(-280, 280)
    meteor.goto(380, y)
    meteorok.append(meteor)
    meteor.reset()


szamlalo = 0


def lepes():
    for m in meteorok:
        m.backward(1)


while True:
    szamlalo += 1
    if szamlalo % 1000 == 0:
        uj_meteor()

    lepes()
    # meteor.backward(0.3)
    space.update()

