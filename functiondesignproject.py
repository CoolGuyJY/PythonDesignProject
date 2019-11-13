#main file
from ArtofCode import*
turtle.colormode(255)
turtle.bgcolor(0,118,206)
bob.speed(0)
bob.pensize(1)

#Arms
qwq.pensize(1)
qwq.right(90)
qwq.color(255,255,255)
for times in range(50):
    qwq.forward(3)
    qwq.right(1)
for times in range(40):
    qwq.forward(2)
    qwq.left(1)
for times in range(30):
    qwq.forward(1)
    qwq.right(1)
   
qwq.penup()
qwq.goto(-60,20)
qwq.pendown()
qwq.pensize(1)
for times in range(50):
    qwq.forward(3)
    qwq.right(1)
for times in range(40):
    qwq.forward(2)
    qwq.left(1)
for times in range(30):
    qwq.forward(1)
    qwq.right(1)

qwq.penup()
qwq.goto(-50,25)
qwq.pendown()
qwq.left(60)
qwq.pensize(2)
for times in range(50):
    qwq.forward(3)
    qwq.right(1)
for times in range(40):
    qwq.forward(2)
    qwq.left(1)
for times in range(30):
    qwq.forward(1)
    qwq.right(1)


qwq.left(40)
qwq.penup()
qwq.goto(-10,20)
qwq.pendown()
qwq.pensize(2)
for times in range(50):
    qwq.forward(3)
    qwq.right(1)
for times in range(40):
    qwq.forward(2)
    qwq.left(1)
for times in range(30):
    qwq.forward(1)
    qwq.right(1)

qwq.penup()
qwq.goto(-20,25)
qwq.pendown()
qwq.left(80)
qwq.pensize(2)
for times in range(50):
    qwq.forward(3)
    qwq.right(1)
for times in range(40):
    qwq.forward(2)
    qwq.left(1)
for times in range(30):
    qwq.forward(1)
    qwq.right(1)

qwq.penup()
qwq.goto(-5,10)
qwq.pendown()
for times in range(50):
    qwq.forward(3)
    qwq.left(1)
for times in range(40):
    qwq.forward(2)
    qwq.right(1)
for times in range(30):
    qwq.forward(1)
    qwq.left(1)

qwq.penup()
qwq.goto(-40,18)
qwq.pendown()
qwq.right(10)
for times in range(50):
    qwq.forward(3)
    qwq.left(1)
for times in range(40):
    qwq.forward(2)
    qwq.right(1)
for times in range(25):
    qwq.forward(1)
    qwq.left(1)

qwq.penup()
qwq.goto(-3,5)
qwq.pendown()
qwq.right(10)
for times in range(50):
    qwq.forward(3)
    qwq.left(1)
for times in range(40):
    qwq.forward(2)
    qwq.right(1)
for times in range(30):
    qwq.forward(1)
    qwq.left(1)

qwq.penup()
qwq.goto(-50,5)
qwq.pendown()
qwq.right(10)
for times in range(50):
    qwq.forward(3)
    qwq.right(1)
for times in range(40):
    qwq.forward(2)
    qwq.left(1)
for times in range(30):
    qwq.forward(1)
    qwq.right(1)



#Bell
bob.penup()
bob.home()
bob.pendown()
bob.pensize(5)
bob.color(222,135,255)
bob.begin_fill()
bob.pencolor(0,185,187)
for times in range(80):
    bob.forward(1)
    bob.left(1)

bob.pensize(3)
for times in range(40):
    bob.forward(1)
    bob.left(2)

for times in range(20):
    bob.forward(1)
    bob.right(2)
    
bob.pensize(4)
for times in range(100):
    bob.forward(1)
    bob.left(1)

for times in range(20):
    bob.forward(1)
    bob.right(1)
    
bob.pensize(5)
for times in range(50):
    bob.forward(1)
    bob.left(2)

for times in range(20):
    bob.forward(2)
    bob.right(1)

bob.right(300)

for times in range(30):
    bob.forward(2)
    bob.left(1)

bob.pensize(5)
for times in range(33):
    bob.forward(1)
    bob.right(2)

bob.home()
bob.right(180)

for times in range(34):
    bob.forward(1)
    bob.right(1)

bob.end_fill()

bob.penup()
bob.goto(-48,100)
bob.pendown()
bob.color(223,220,255)
bob.circle(10)

bob.penup()
bob.goto(0,100)
bob.pendown()
bob.color(223,220,255)
bob.circle(10)

bob.penup()
bob.goto(40,60)
bob.pendown()
bob.color(223,220,255)
bob.right(20)
bob.forward(10)

bob.penup()
bob.goto(23,60)
bob.pendown()
bob.color(223,220,255)
bob.right(10)
bob.forward(10)

bob.pensize(2)
bob.penup()
bob.goto(-30,60)
bob.pendown()
bob.circle(3)

#liljellyfish
qwq.penup()
qwq.goto(400,0)
qwq.pendown()
qwq.pensize(1)
qwq.color("white")
for times in range(30):
    qwq.forward(2)
    qwq.right(2)
for times in range(20):
    qwq.forward(2)
    qwq.left(1)
for times in range(12):
    qwq.forward(1)
    qwq.right(3)

qwq.penup()
qwq.goto(410,0)
qwq.pendown()
qwq.left(30)
for times in range(30):
    qwq.forward(2)
    qwq.right(2)
for times in range(20):
    qwq.forward(2)
    qwq.left(2)
for times in range(12):
    qwq.forward(1)
    qwq.right(3)

qwq.penup()
qwq.goto(415,10)
qwq.pendown()
for times in range(30):
    qwq.forward(2)
    qwq.left(2)
for times in range(20):
    qwq.forward(2)
    qwq.right(2)
for times in range(12):
    qwq.forward(1)
    qwq.left(3)

qwq.right(60)
qwq.penup()
qwq.goto(380,0)
qwq.pendown()
qwq.pensize(4)
qwq.right(30)

qwq.color(222,135,255)
qwq.begin_fill()
qwq.pencolor(0,185,187)
for times in range(60):
    qwq.forward(1)
    qwq.right(2)

for times in range(10):
    qwq.forward(1)
    qwq.left(2)

for times in range(70):
    qwq.forward(1)
    qwq.right(2)

for times in range(20):
    qwq.forward(1)
    qwq.left(2)

for times in range(20):
    qwq.forward(1)
    qwq.right(2)

qwq.right(60)
for times in range(50):
    qwq.forward(1)
    qwq.right(1)

for times in range(15):
    qwq.forward(1)
    qwq.left(2)

for times in range(10):
    qwq.forward(1)
    qwq.right(2)

qwq.end_fill()
qwq.hideturtle()

#bubbles
bob.penup()
bob.goto(-100,300)
bob.pendown()
bob.pensize(2)
bob.color(209,255,255)
bob.circle(20)
bob.penup()
bob.goto(-110,300)
bob.pendown()
bob.right(90)
bob.forward(5)

bob.penup()
bob.goto(200,270)
bob.pendown()
bob.pensize(2)
bob.color(209,255,255)
bob.circle(20)
bob.penup()
bob.goto(210,290)
bob.pendown()
bob.right(90)
bob.forward(5)

bob.penup()
bob.goto(250,-155)
bob.pendown()
bob.pensize(2)
bob.color(209,255,255)
bob.circle(20)
bob.penup()
bob.goto(250,-135)
bob.pendown()
bob.right(110)
bob.forward(5)

bob.penup()
bob.goto(180,-155)
bob.pendown()
bob.pensize(2)
bob.color(209,255,255)
bob.circle(15)
bob.penup()
bob.goto(190,-160)
bob.pendown()
bob.right(70)
bob.forward(5)


#star
bob.penup()
bob.goto(250,200)
bob.pendown()
bob.color(245,188,106)
bob.begin_fill()
for times in range(5):
    bob.forward(50)
    bob.right(144)
bob.end_fill()

bob.penup()
bob.goto(-250,180)
bob.pendown()
bob.color(245,188,106)
bob.begin_fill()
for times in range(5):
    bob.forward(30)
    bob.right(144)
bob.end_fill()

bob.penup()
bob.goto(-250,120)
bob.pendown()
bob.color(245,188,106)
bob.begin_fill()
for times in range(5):
    bob.forward(30)
    bob.right(144)
bob.end_fill()

bob.penup()
bob.goto(-220,150)
bob.pendown()
bob.color(245,188,106)
bob.begin_fill()
for times in range(5):
    bob.forward(30)
    bob.right(144)
bob.end_fill()

bob.penup()
bob.goto(220,150)
bob.pendown()
bob.color(245,188,106)
bob.begin_fill()
for times in range(5):
    bob.forward(30)
    bob.right(144)
bob.end_fill()

bob.hideturtle()




