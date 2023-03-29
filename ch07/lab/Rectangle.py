class Rectangle: 
    def __init__(self, x=0,y=0, h=1, w=1): 
        self.x = abs(x)  
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        """
        this function takes the self instance being created and returns a string reporting the values of the instance
        args: instance (self)
        result: str (values of instance)
        """
        return f"x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width}"
