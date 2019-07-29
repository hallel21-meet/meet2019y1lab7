import turtle
turtle.goto(0,0)
UP=0
DOWN=1
RIGHT=2
LEFT=3

direction = UP
def up():
    global direction
    direction = UP
    print("you pressed the up key.")
    on_move()

def down():
    global direction
    direction = DOWN
    on_move()

def left():
    global direction
    direction = LEFT
    on_move()

def right():
    global direction
    direction = RIGHT
    on_move()

turtle.onkey(up,"Up")
turtle.goto(0,0)
turtle.listen()

def on_move():
    turtle.pos()
    x,y = turtle.pos()
    if direction == UP:
        turtle.goto(x, y+50)
    elif direction == DOWN:
        turtle.goto(x, y-50)
    elif direction == "Left":
        turtle.goto(x-50, y)
    elif direction == "Right":
        turtle.goto(x+50, y)

turtle.onkey(on_move,"Up")
turtle.onkey(on_move,"Down")
turtle.onkey(on_move,"Left")
turtle.onkey(on_move,"Right")
turtle.mainloop()
