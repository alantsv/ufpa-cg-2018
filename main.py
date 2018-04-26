#!/usr/bin/python3

__author__ = "Alan Veloso"

from Point import Point
from Circle import Circle
from Straight import Straight
import matplotlib.pyplot as plt
from Curve import *
from Range import range
import Fill
from Clip import cohenSutherland
import Transformation

def draw(makePoints, name = 'figure.png'):
  plt.cla()
  plt.plot(list(point.x for point in makePoints), list(point.y for point in makePoints), 'bs')
  #if (min(makePoints) > Point(0,0)):
    #plt.axis([-1, (max(makePoints, key=lambda x:x.x).x) + 1, -1 , max(makePoints, key=lambda y:y.y).y + 1])
  #else:
    #plt.axis([min(makePoints).x - 1, max(makePoints).x + 1, min(makePoints).y - 1, max(makePoints).y + 1])
  plt.savefig(name)

def main():

  hexagon = Straight(Point(0, 2), Point(2, 4)).make() + Straight(Point(2, 4), Point(4, 4)).make() + Straight(Point(4, 4), Point(6, 2)).make()  + Straight(Point(6, 2), Point(4, 0)).make() + Straight(Point(4, 0), Point(2, 0)).make() + Straight(Point(2, 0), Point(0, 2)).make()
  print("Hexagon points:\n" + str(hexagon))
  draw(hexagon, "hexagon.png")
  
  hexagonTranslated = Transformation.translate(hexagon, 1, 2)
  print("Translated hexagon points:\n" + str(hexagonTranslated))
  draw(hexagonTranslated, "hexagonTranslated.png")
  
  hexagonRotated = Transformation.rotate(hexagon, 45)
  print("Rotated hexagon points:\n" + str(hexagonRotated))
  draw(hexagonRotated, "hexagonRotated.png")
  
  hexagonScalated = Transformation.scale(hexagon, 2)
  print("Scalated hexagon points:\n" + str(hexagonScalated))
  draw(hexagonScalated, "hexagonScalated.png")
  

  poligon = [Point(0, 10), Point(40, 30)], [Point(40, 30), Point(20, 50)] ,[Point(20, 50), Point(60, 70)], [Point(60, 70), Point(110, 30)], [Point(110, 30), Point(130, 0)], [Point(130, 0), Point(100, 30)], [Point(100, 30), Point(80, 0)], [Point(80, 0), Point(0, 10)]
  draw(Straight(Point(0, 10), Point(40, 30)).make() + Straight(Point(40, 30), Point(20, 50)).make() + Straight(Point(20, 50), Point(60, 70)).make() + Straight(Point(60, 70), Point(110, 30)).make() + Straight(Point(110, 30), Point(130, 0)).make() + Straight(Point(130, 0), Point(100, 30)).make() + Straight(Point(100, 30), Point(80, 0)).make() + Straight(Point(80, 0), Point(0, 10)).make(), "poligon.png")
  poligonFill = Fill.scanline(poligon)
  print(poligonFill)
  
  draw(poligonFill, "poligonFill.png")

  circle = Circle(50).make()
  print("Circle points:\n" + str(circle))
  draw(circle, "circle.png")
  
  curve = Curve([Point(0,0), Point(1,5), Point(2,0), Point(3,3)]).make()
  print ("Curve points:\n" + str(curve))
  draw(curve, "curve.png")
  
  fill = []
  Fill.recursive(Point(2, 3), hexagon, fill)
  draw(hexagon + fill, "hexagonFill.png")
  #print(cohenSutherland(Point(3, 1), Point(5, 4), 2, 4, 2, 4))

if __name__ == "__main__":
  main()