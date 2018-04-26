from Point import Point
import math

def translate(points, tx, ty):
  return list(Point(point.x, point.y) + Point(tx, ty) for point in points)
  
def rotate(points, rotationDegree):
  degreeCos = math.cos(math.radians(rotationDegree))
  degreeSin = math.sin(math.radians(rotationDegree))
  return list(Point(point.x * degreeCos - point.y * degreeSin, point.y * degreeCos + point.x * degreeSin) for point in points)

def scale(points, scaleFactor):
  return list(Point(point.x,  point.y) * scaleFactor for point in points)