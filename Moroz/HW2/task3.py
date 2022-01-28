import turtle
t = turtle
t.pensize(5)
t.color('black', 'yellow')

# circle
t.begin_fill() 
t.circle(100) 
t.end_fill() 
t.penup()

#left dot
t.goto(-35, 135)
t.pendown()
t.dot(30)
t.penup()

#right dot
t.goto(35, 135)
t.pendown()
t.dot(30)
t.penup()

#mouth
t.fillcolor('red')
t.goto(-60, 60)
t.pendown()
t.setheading(-60)
t.begin_fill()
t.circle(70, 120)
t.goto(-60, 60)
t.end_fill()



t.done()


