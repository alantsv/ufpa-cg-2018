from Point import Point

def reflect(p1, p2):
	invertedX, invertedY, swappedXY = False, False, False

	m = (p2.y - p1.y) / (p2.x - p1.x)

	if ((m > 1) or (m < -1)):
		p1.x, p1.y, p2.x, p2.y = p1.y, p1.x, p2.y, p2.x
		swappedXY = True
	if (p1.x > p2.x):
		p1.x = -p1.x
		p2.x = -p2.x
		invertedX = True
	if (p1.y > p2.y):
		p1.y = -p1.y
		p2.y = -p2.y
		invertedY = True
	return invertedX, invertedY, swappedXY


def undoReflect(Points, invertedX, invertedY, swappedXY):
	pointsReturned = Points
	if invertedY == True:
		pointsReturned = list(
		    Point(point.x, -point.y) for point in pointsReturned)
	if invertedX == True:
		pointsReturned = list(
		    Point(-point.x, point.y) for point in pointsReturned)
	if swappedXY == True:
		pointsReturned = list(
		    Point(point.y, point.x) for point in pointsReturned)
	return pointsReturned


def bresenham(point1, point2):
	p1 = Point(point1.x, point1.y)
	p2 = Point(point2.x, point2.y)
	invertedX, invertedY, swappedXY = reflect(p1, p2)
	x, y = p1.x, p1.y
	deltaX = p2.x - p1.x
	deltaY = p2.y - p1.y
	m = deltaY / deltaX

	e = m - 1 / 2

	straightStitches = []
	straightStitches.append(Point(x, y))

	while x < p2.x:
		if e >= 0:
			y += 1
			e -= 1
		x += 1
		e += m
		straightStitches.append(Point(x, y))

	return undoReflect(straightStitches, invertedX, invertedY, swappedXY)

class Straight:
  extremeA = Point()
  extremeB = Point()
  
  def __init__(self, point1, point2):
    self.extremeA = Point(point1.x, point1.y)
    self.extremeB = Point(point2.x, point2.y)
    
  def make(self):
    return bresenham(self.extremeA, self.extremeB)
