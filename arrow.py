# ArrowDraw.py
import turtle
Screen = turtle.Screen()
t = turtle.Pen()
turtle.speed(0)
turtle.turtlesize(2,2,2)

def up():
    turtle.forward(50)
def left():
    turtle.left(90)
def right():
    turtle.right(90)
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(turtle.penup(),"p")
turtle.listen()
Screen.mainloop()

