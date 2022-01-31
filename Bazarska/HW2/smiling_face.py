import turtle 
t=turtle.Turtle()
t.color('black', 'yellow')
t.pensize(5)

t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

#left eye
t.goto(-30, 135)
t.pendown()
t.dot(25)
t.penup()

#right eye
t.goto(30, 135)
t.pendown()
t.dot(25)
t.penup()

#mouth
t.goto(-55, 95)
t.pendown()
t.setheading(-90)
t.circle(-30,50)
t.penup()

t.goto(-60, 80)
t.pendown()
t.setheading(-60)
t.circle(70, 120)
t.penup()

t.goto(75, 72)
t.pendown()
t.setheading(-10)
t.circle(30, -50)
t.penup
 
