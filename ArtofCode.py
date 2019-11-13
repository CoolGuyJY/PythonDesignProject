#function files
import turtle
bob=turtle.Turtle()
turtle.colormode(255)
qwq = turtle.Turtle()

def explosion(d):
    for times in range(100):
        bob.color(255,195-times*1,140-times*1)
        bob.forward(100)
        bob.right(799)
        bob.forward(100)
        bob.right(799)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown() 

def ball(d):
    bob.color(255,90,130)
    bob.begin_fill()
    bob.circle(100)
    bob.end_fill()

def line(d):
    for times in range(200):
        bob.forward(d)
        bob.left(599)
