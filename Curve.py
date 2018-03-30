from Point import Point
from Range import range

def bazierPoint(controlPt, t):
  n = len(controlPt)
  pts = [None] * (n + 1)
  for i in range(0, n):
    pts[i] = controlPt[i]
    
  for r in range(1, n+1):
    for i in range(0, n-r):
      pts[i] = (1-t)*pts[i] + t*pts[i+1]
      
  return pts[0]

class Curve:
  controlPt = []
  
  def __init__ (self, _controlPt):
    self.controlPt = _controlPt

  def draw(self, step = 0.01):
    curvePoints = []
    for t in range(0, 1, step):
      curvePoints.append(bazierPoint(self.controlPt, t))
  
    return curvePoints
     