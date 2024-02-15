import math

def degree_to_radian(degrees):
    return math.radians(degrees)


degrees = 45
radians = degree_to_radian(degrees)
print(f"{degrees} is {radians:.2f} .")



def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

p1= 5
p2 = 7
height = 4

area = trapezoid_area(p1, p2, height)
print(area)





import math

def regular_polygon_area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))


s = 4
l = 25

area = regular_polygon_area(s, l)
print( int(area))




def parallelogram_area(l, h):
    return l * h


l = 6
h = 8

area = parallelogram_area(l, h)
print( area)

