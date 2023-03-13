import turtle 
import random 


pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("Orange")
pen.shape("turtle")
pen.color("Black")
pen.speed(0) #Fastest Speed

distance = 10
angle = 90
is_in_screen = True


while is_in_screen:
    coin = random.randrange(0,2) #Either 0 (false) or 1 
    if coin: #heads 0 = false 
        pen.right(angle)
    else:
        pen.left(angle)
    pen.forward(distance)

    turtleX = pen.xcor()
    turtleY = pen.ycor()
    x_range = screen.window_width() / 2
    y_range = screen.window_height() / 2

    if abs(turtleX) > x_range or abs(turtleY) > y_range: 
        is_in_screen = False


screen.exitonclick()

