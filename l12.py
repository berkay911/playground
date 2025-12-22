from device_list import Device

calculator = Device("Casio")
oscilloscope = Device("Agilent")

#print(calculator.brand)
#print(oscilloscope.brand)
#print(calculator.device_type)
#print(oscilloscope.device_type)

#print(calculator._is_on)

#calculator.turn_on()
#print(calculator._is_on)
#-----------------------------------------#


from geometry import Coordinate, Circle

coord1 = Coordinate(3,4)
coord2 = Coordinate(7,8)
coord_origin = Coordinate(0,0)

#print(coord1.x)
#print(coord1.y)
#print(coord2.print_coordinates())
#print(coord1.distance_to_origin())

#print(coord1.distance_to(coord2))

circle1 = Circle(coord1, 5)
circle2 = Circle(coord_origin, 3)

#print(circle1.radius)
#print(circle2.center)

print(Coordinate.distance_to(circle1.center, circle2.center))
print(circle1.center.distance_to_origin())

print(circle1.area())

coord3 = Coordinate(5,1)
print(circle1.is_inside(coord1))
print(circle2.is_inside(coord3))

print(circle2)


print(circle1.mirror())