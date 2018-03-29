#!/usr/bin/python3

__auhor__ = "Veloso, Alan"

import matplotlib.pyplot as plt
from Bresenham import bresenham
from Point import Point

def main():
	p1 = Point(0, 2)
	p2 = Point(2, 4)
	p3 = Point(4, 4)
	p4 = Point(6, 2)
	p5 = Point(4, 0)
	p6 = Point(2, 0)

	hexagonStraight = []
	hexagonStraight = bresenham(p1, p2) + bresenham(p2, p3) + bresenham(
	    p3, p4) + bresenham(p4, p5) + bresenham(p5, p6) + bresenham(p6, p1)

	print(hexagonStraight)
	plt.plot(
	    list(point.x for point in hexagonStraight),
	    list(point.y for point in hexagonStraight), 'bs')
	plt.savefig('hexagon.png')


if __name__ == "__main__":
	main()
