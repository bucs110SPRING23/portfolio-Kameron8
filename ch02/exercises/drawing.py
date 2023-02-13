import turtle

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of sides: "))

pen = turtle.Turtle()
pen.color("Pink")

window = turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.left(360/sides)


window.exitonclick()
