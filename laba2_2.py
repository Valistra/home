import turtle


turtle.position()

turtle.circle(20, 180)
turtle.circle(20, 180)


turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()
c=10
b=-250
x=0
while x<10:
    turtle.forward(c)
    turtle.right(-90)
    turtle.forward(c)
    turtle.right(-90)
    turtle.forward(c)
    turtle.right(-90)
    turtle.forward(c)
    turtle.right(-90)
    c+=20
    turtle.penup()
    b-=10
    turtle.goto(b, b)
    turtle.pendown()
    x+=1
    
