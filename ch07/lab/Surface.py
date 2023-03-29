import Rectangle

class Surface: 
    def __init__(self, filename,  x=0,y=0, h=1, w=1): 
        self.rect = Rectangle.Rectangle(x, y, h, w)
        self.image = str(filename)


    def getRect(self):
        """
        this function allows for the values from the Rectangle class to be returned 
        args: instance (self)
        result: int (dimensions of a rectangle)
        """
        return self.rect
