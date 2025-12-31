from Graphics import rectangle, circle
from Graphics.ThreeDgraphics import cuboid, sphere
# Rectangle
length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
print("Rectangle Area:", rectangle.area(length, breadth))
print("Rectangle Perimeter:", rectangle.perimeter(length, breadth))
# Circle
radius = int(input("\nEnter radius of circle: "))
print("Circle Area:", circle.area(radius))
print("Circle Perimeter:", circle.perimeter(radius))
# Cuboid
length = int(input("\nEnter length of cuboid: "))
breadth = int(input("Enter breadth of cuboid: "))
height = int(input("Enter height of cuboid: "))
print("Cuboid Surface Area:", cuboid.Surface_area(length, breadth, height))
print("Cuboid Volume:", cuboid.Volume(length, breadth, height))
# Sphere
radius = int(input("\nEnter radius of sphere: "))
print("Sphere Surface Area:", sphere.surface_area(radius))
print("Sphere Volume:", sphere.volume(radius))
