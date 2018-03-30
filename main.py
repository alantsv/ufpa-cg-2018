#!/usr/bin/python3

__author__ = "Alan Veloso"

from Point import Point
from Circle import Circle
from Bresenham import bresenham
import matplotlib.pyplot as plt
from Curve import *
from Range import range

def drawHexagon():
  p1 = Point(0, 2)
  p2 = Point(2, 4)
  p3 = Point(4, 4)
  p4 = Point(6, 2)
  p5 = Point(4, 0)
  p6 = Point(2, 0)
  
  hexagonStraight = []
  hexagonStraight = bresenham(p1, p2) + bresenham(p2, p3) + bresenham(
	    p3, p4) + bresenham(p4, p5) + bresenham(p5, p6) + bresenham(p6, p1)

  print("Hexagon points:\n" + str(hexagonStraight))
  plt.plot(
    list(point.x for point in hexagonStraight), list(point.y for point in hexagonStraight), 'bs')
  plt.savefig('hexagon.png')

def drawCircle():
  circle = Circle(5) # radius = 5
  drawPoints = circle.draw()
  print ("Cirle points:\n" + str(drawPoints))
  plt.cla()
  plt.plot(list(point.x for point in drawPoints), list(point.y for point in drawPoints), 'bs')
  plt.savefig('circle.png')

def drawCurve():
  curve = Curve([Point(0,0), Point(1,5), Point(2,0), Point(3,3)])
  drawPoints = curve.draw()
  print ("Curve points:\n" + str(drawPoints))
  plt.cla()
  plt.plot(list(point.x for point in drawPoints), list(point.y for point in drawPoints), 'bs')
  plt.savefig('curve.png')


def main():
  drawHexagon()
  drawCircle()
  drawCurve()

if __name__ == "__main__":
  main()