import turtle
turtle.Screen().bgcolor("black")
turtle.setup(1000, 600)
turtle.penup()
turtle.fd(150)
turtle.right(90)
turtle.fd(50)
turtle.right(90)
turtle.pendown()
turtle.pencolor("#d43531")
turtle.fillcolor('#d43531')
turtle.begin_fill()
for i in range(2):
    turtle.fd(300)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
turtle.end_fill()
turtle.pencolor("white")
turtle.fillcolor('white')
turtle.begin_fill()
turtle.left(270)
turtle.penup()
turtle.fd(100)
turtle.pendown()
for i in range(2):
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(300)
    turtle.left(90)
turtle.end_fill()

turtle.left(180)
turtle.penup()
turtle.fd(150)
turtle.right(90)
turtle.fd(250)

turtle.write("Lengyelország",font=('Arial' ,20, 'normal'))

turtle.hideturtle()
turtle.done()