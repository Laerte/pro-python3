from collections import namedtuple

Point = namedtuple('Point', 'x y')
point = Point(13, 25)

print(point)

print(point.x, point.y)

print(point[0], point[1])
