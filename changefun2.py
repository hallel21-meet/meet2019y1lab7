import turtle
turtle.goto(0,0)
UP=0
DOWN=1
LEFT=2
RIGHT=3
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
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.listen()

def on_move():
    turtle.pos()
    x,y = turtle.pos()
    if direction == UP:
        turtle.goto(x, y+50)
    elif direction == DOWN:
        turtle.goto(x, y-50)
    elif direction == LEFT:
        turtle.goto(x-50, y)
    elif direction == RIGHT:
        turtle.goto(x+50, y)


turtle.mainloop()
