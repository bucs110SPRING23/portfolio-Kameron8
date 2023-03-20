import turtle 
import random
import math

def pizza_size(size= "small"):
    """
    this function takes the user input and translates it into a size of the pizza 
    args: str ("small", "medium", or "large")
    return: int (crust_diameter)

    """
    if size == "small":
        crust_diameter = 300
        return crust_diameter
    
    elif size == "medium":
        crust_diameter = 400
        return crust_diameter
    
    elif size == "large":
        crust_diameter = 450
        return crust_diameter
       

def crust(crust_diameter=300):
    """
    this function takes the diameter of the crust and shrinks it down a bit to make the cheese of the pizza
    args: int (crust_diameter)
    result: float (cheese_diameter)
    """
    crust_pen = turtle.Turtle()
    crust_pen.color("Sandy Brown")
    crust_pen.dot(crust_diameter)
    cheese_diameter = crust_diameter / 1.1
    cheese_pen = turtle.Turtle()
    cheese_pen.color("Gold")
    cheese_pen.dot(cheese_diameter)
    return cheese_diameter


def placing_pepperoni(pepperoni="yes", cheese_diameter=300/1.1):
    """
    this function allows the user to select whether to put pepperoni on their pizza or not 
    arg: str ("yes" or anything else)
    result: float (cheese_diameter)
    """
    if pepperoni == "yes":
        width, height = turtle.screensize()
        pepperoni_pen = turtle.Turtle()
        pepperoni_diameter = 35
        pepperoni_pen.color("Tomato2")
        count = 0
        while count < cheese_diameter / 20:
            x_pepperoni = random.randrange(-1 * width, width)
            y_pepperoni = random.randrange(-1 * height, height)
            distance_from_center = math.hypot(x_pepperoni, y_pepperoni)
            on_pizza = distance_from_center <= cheese_diameter / 2 - pepperoni_diameter
            if on_pizza == True:
                pepperoni_pen.up()
                pepperoni_pen.goto(x_pepperoni,y_pepperoni)
                pepperoni_pen.down()
                pepperoni_pen.dot(pepperoni_diameter)
                count += 1
            else:
                pass
    else:
        pass
    return cheese_diameter


def cuttingpizza(number_of_slices=6, cheese_diameter=300/1.1):
     """
     this function allows the user to select how many slices to cut their pizza into
     args: int (number_of_slices), float (cheese_diameter)
     result: none
     """
     pizzacutter_pen = turtle.Turtle()
     pizzacutter_pen.color("Black")
     for i in range(1, number_of_slices + 1): 
          pizzacutter_pen.right(360/number_of_slices)
          pizzacutter_pen.forward(cheese_diameter / 2)
          pizzacutter_pen.goto(0,0)
          

def main():
    window = turtle.Screen()
    turtle.bgcolor("Peach Puff")
    size = (input("Pick a Size (small, medium, large): "))
    crust_diameter = pizza_size(size)
    cheese_diameter = crust(crust_diameter)
    pepperoni = input("Would you like pepperoni? ")
    placing_pepperoni(pepperoni, cheese_diameter)
    number_of_slices = int(input("How many slices? "))
    cuttingpizza(number_of_slices, cheese_diameter)
    print("Here is your", size, "pizza, cut into", number_of_slices, "slices! Hope you enjoy!")
    window.exitonclick()


main()