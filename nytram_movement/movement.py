from .direction import Direction

from nytram.engine import Time
from nytram.vector import Vec3

from kao_decorators import proxy_for

@proxy_for("directions", ["__getitem__"])
class Movement:
    """ Represents Movement behavior for an Entity """
    
    def __init__(self, directions, speed=1):
        """ Initialize the movement with the directions it can move in and the speed to move at """
        self.directions = {key:Direction(directions[key]) for key in directions}
        self.speed = speed
    
    def update(self):
        """ Update the behavior """
        self.direction = sum([direction.directionVector for direction in self.directions.values()], Vec3(0,0,0))
        self.entity.transform.position += (self.direction*(self.speed*Time.sinceLastFrame()/1000.0))
        
    def __setitem__(self, key, value):
        """ Return the item for the key """
        self.directions[key] = Direction(value)