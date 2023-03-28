class Rectangle: 
    def __init__(self, x=0,y=0, h=1, w=1): 
        self.x = abs(x)  
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width}"
