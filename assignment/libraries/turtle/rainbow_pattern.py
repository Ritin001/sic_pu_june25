import turtle
colours=['red' , 'yellow', 'blue', 'orange', 'green', 'red']
aiden = turtle.Turtle()
turtle.bgcolor('black')#make bg black


#make  36 regular hexagon 10 degree apart
for n in range(36):
    #make hexagon by repeating 6 times
    for i in range(6):
        aiden.color(colours[i])
        aiden.forward(100)
        aiden.left(60)
    #add a turn before next hexagon
    aiden.right(10)

#getting ready to draw  36 circles
aiden.penup()
aiden.color('white')

#repeat 36 times to match 36 hexagon
for i in range(36):
    aiden.forward(220)
    aiden.pendown()
    aiden.circle(5)
    aiden.penup()
    aiden.backward(220)
    aiden.right(10)

#hide the turtle
aiden.hideturtle()
