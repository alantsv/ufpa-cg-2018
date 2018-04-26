from Point import Point
from math import floor

def recursive(point, edgePoints, fillPoints):
  current = Point(point.x, point.y)
  if ((not (current in edgePoints)) and  (not (point in fillPoints))):
    fillPoints.append(point)
    recursive(Point(point.x+1, point.y), edgePoints, fillPoints)
    recursive(Point(point.x, point.y+1), edgePoints, fillPoints)
    recursive(Point(point.x-1, point.y), edgePoints, fillPoints)
    recursive(Point(point.x, point.y-1), edgePoints, fillPoints)

def filterPoints(points, sides):
  poitsFiltered = []
  for point in points:
    for side in sides:
      sideSorted = sorted(side, key=lambda x:x.x)
      if (point == sideSorted[0]) or (point == sideSorted[1]):
        poitsFiltered.append(point)
        break
      m1 = (sideSorted[1].y - sideSorted[0].y)/(sideSorted[1].x - sideSorted[0].x)
      m1 = float('%.1f'%(m1))
      try:
        m0 = (sideSorted[1].y - point.y)/(sideSorted[1].x - point.x)
      except:
       m0 = (point.y - sideSorted[0].y)/(point.x - sideSorted[0].x)
      m0 = float('%.1f'%(m0))
      if (point.x >= sideSorted[0].x) and (point.x < sideSorted[1].x) and ((point.y >= sideSorted[0].y) and (point.y < sideSorted[1].y) or (point.y >= sideSorted[1].y) and (point.y < sideSorted[0].y)) and m1 == m0:
        poitsFiltered.append(point)
        break
      
  return poitsFiltered

def scanline(sides):
  sidesTable = [[] for _ in range(len(sides))]
  i = 0
  for side in sides:
    sidesTable[i].append(min(side, key=lambda x:x.y).y)
    sidesTable[i].append(max(side, key=lambda x:x.y).y)
    sidesTable[i].append(min(side, key=lambda x:x.y).x)
    sidesTable[i].append(1/((side[0].y - side[1].y) / (side[0].x - side[1].x)))
    i+=1
    
  interScanLine = []
  scanLine = 0
  for scanLine in range(min(sidesTable, key=lambda x:x[0])[0], max(sidesTable, key=lambda x:x[1])[1]):
    for line in sidesTable:
      x = Point(line[3] * (scanLine - line[0]) + line[2], scanLine)
      interScanLine.append(x)
  
  poitsFiltered = filterPoints(interScanLine, sides)
  #poitsFiltered = interScanLine
  return poitsFiltered
  