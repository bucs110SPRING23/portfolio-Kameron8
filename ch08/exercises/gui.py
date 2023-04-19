
class Mario: 
    def __init__(self, x=0, y=0, score=0, color="red" ):
        """
        initializes the mario object 
        args: x[int] y[int] player's positon, score[int] player's score, color[str] color of the player
        """
        self.pos = (x,y) #Character's position 
        self.score = score #Players score
        self.color = color #Players color

class Enemy: 
    def __init__(self, speed=0, x=0, y=0):
        """
        initializes enemy object
        args: speed[int] speed the enemy is going, x[int], y[int] enemy's position 
        """
        self.pos = (x,y) #What is the enemy's position
        self.speed = speed #What speed is the enemy using 
        self.alive = True #Is the enemy alive?

class Questionblock: 
    def __init__(self, item= "coin", x=0, y=0): 
        """
        intializes the question block object 
        args: item [str], x[int], y[int], block's position 
        """
        self.broken = False #Does the brick contain a coin?
        self.item = item #Does the brick contain a mushroom?
        self.pos = (x,y) #Has the block already been hit?
