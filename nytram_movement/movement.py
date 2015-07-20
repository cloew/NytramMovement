from .direction import Direction
from .speed import Speed

from nytram.vector import Vec3

from kao_decorators import proxy_for

@proxy_for("directions", ["__getitem__"])
class Movement:
    """ Represents Movement behavior for an Entity """
    
    def __init__(self, directions, speed=1):
        """ Initialize the movement with the directions it can move in and the speed to move at """
        self.directions = {key:Direction(directions[key]) for key in directions}
        self.speed = Speed(speed)
    
    def update(self):
        """ Update the behavior """
        self.direction = sum([direction.directionVector for direction in self.directions.values()], Vec3(0,0,0))
        self.speed.apply(self.entity.transform, self.direction)
        
    def __setitem__(self, key, value):
        """ Return the item for the key """
        self.directions[key] = Direction(value)