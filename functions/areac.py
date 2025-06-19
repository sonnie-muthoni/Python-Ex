#calculate the area of a circle
def area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area
radius = float(input("Enter the radiuis of the circle: "))
ouput =area(radius)
print ("the area of the circle is:", ouput)

