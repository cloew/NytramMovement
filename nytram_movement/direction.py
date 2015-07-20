from nytram.vector import Vec3

class Direction:
    """ Represents a direction an entity can move in """
    NO_MOVEMENT = Vec3(0,0,0)
    
    def __init__(self, direction):
        """ Initialize with the direction vector to use """
        self.direction = Vec3(direction).unitVector
        self.moving = False
        
    def toggle(self, event=None):
        """ Toggle whether this direction is being used for movement """
        self.moving = not self.moving
        
    @property
    def directionVector(self):
        """ Return the direction vector """
        return self.direction if self.moving else self.NO_MOVEMENT