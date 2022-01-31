from turtle import *

hideturtle()
up()
goto(0, -100)
width(5)
down()

begin_fill()
fillcolor("yellow")
circle(110)
end_fill()

up()
goto(-67, -40)
setheading(-60)
width(5)
down()
circle(80, 120)

fillcolor("black")
for i in range(-35, 105, 70):
    up()
    goto(i, 35)
    setheading(0)
    down()
    begin_fill()
    circle(10)
    end_fill()

done()
