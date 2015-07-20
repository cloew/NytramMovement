from nytram.engine import Time

class Speed:
    """ Represents a basic speed class """
    
    def __init__(self, speed):
        """ Initialize with the speed value """
        self.speed = speed
        
    def apply(self, transform, direction):
        """ Apply the speed in the given direction to the given transform """
        transform.position += (direction*(self.speed*Time.sinceLastFrame()/1000.0))