import turtle
x1=0
b1=20
turtle.position()





turtle.shape("turtle")
turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()


turtle.forward(50)
turtle.right(-90)
turtle.forward(50)
turtle.right(-90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)




turtle.penup()
turtle.home()
turtle.pendown()
x=0
b=20
while x<40:
    turtle.forward(b)
    turtle.right(-90)
    x+=1
    b+=5
 
turtle.penup()
turtle.goto(250, 250)
turtle.pendown()

while x1<30:
    turtle.circle(b1, 180)
    x1+=1
    b1=b1+5


print ("End")    
