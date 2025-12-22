class Coordinate(object):
    def __init__ (self, x,y):
        self.x = x
        self.y = y
    def print_coordinates(self):
        return (f"Coordinates are: ({self.x}, {self.y})")
    def distance_to_origin(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    def distance_to(self, other):
        import math
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
class Circle(object):
    def __init__ (self, center, radius):
        self.center = center  # center will have to be a Coordinate instance
        self.radius = radius   #integer or float
    
    def __str__(self):
        return (f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}")



    def area(self):
        import math
        return math.pi * (self.radius**2)
    def is_inside(self, coord_input):
        distance = self.center.distance_to(coord_input)
        return distance < self.radius
    def mirror(self):
        (self.center.x, self.center.y) = (self.center.y, self.center.x)
        return self

        
