from Point import Point

class Circle:
  radius = 0
  center = Point()
  
  def __init__(self, radius = 1, center = Point()):
    self.radius = radius
    self.center = Point(center)
  
  def reflectOctant(self, firstOctant):
    otherOctant = []
    # second octant (y, x)
    for point in firstOctant:
      otherOctant.append(Point(point.y, point.x))
    # third octant (y, -x)
    for point in firstOctant:
      otherOctant.append(Point(point.y, -point.x))
    # fourth octant (x, -y)
    for point in firstOctant:
      otherOctant.append(Point(point.x, -point.y))
    # fifth octant (-x, -y)
    for point in firstOctant:
      otherOctant.append(Point(-point.x, -point.y))
    # sixth octant (-y, -x)
    for point in firstOctant:
      otherOctant.append(Point(-point.y, -point.x))
    # seventh octant (-y, x)
    for point in firstOctant:
      otherOctant.append(Point(-point.y, point.x))
    # eighth octant (-x, y)
    for point in firstOctant:
      otherOctant.append(Point(-point.x, point.y))

    
    return otherOctant
    
  
  def draw(self):
    x = 0
    y = self.radius
    p = 1 - self.radius
    firstOctant = []
    firstOctant.append(Point(x, y))
    
    while (x < y):
      x+=1
      if (p < 0):
        p+= 2*x + 3
      else:
        y-=1
        p+= 2*x - 2*y + 5
      firstOctant.append(Point(x,y))
        
    drawPoints = firstOctant
    drawPoints.extend(self.reflectOctant(firstOctant))
    return drawPoints
    
    