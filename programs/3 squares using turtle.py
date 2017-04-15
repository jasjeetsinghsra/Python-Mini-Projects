from turtle import Turtle, Screen
import random
def squares():
    playground=Screen()
    playground.bgcolor("black")
    timmy=Turtle()
    timmy.shape("turtle")
    timmy.color("red")
    timmy.speed(1)
    turtle.colormode(255)
    for j in range(0,1):
        r = random.randrange(0, 255,10)
        g = random.randrange(0, 255,10)
        b = random.randrange(0, 255,10)
        timmy.pencolor((r,g,b))
        for i in range(0,4):
            timmy.forward(100)
            timmy.left(90)
        timmy.right(1)
    timm=Turtle()
    timm.shape("turtle")
    timm.color("red")
    timm.speed(1)
    turtle.colormode(255)
    for j in range(0,1):
        r = random.randrange(0, 255,10)
        g = random.randrange(0, 255,10)
        b = random.randrange(0, 255,10)
        timm.pencolor((r,g,b))
        for i in range(0,4):
            timm.forward(200)
            timm.left(90)
        timm.right(1)
    t=Turtle()
    t.pencolor("red")
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    playground.exitonclick()

squares()
