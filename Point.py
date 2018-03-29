class Point:
  x, y = 0, 0
  
  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y
  
  def __str__ (self):
    return (str((self.x, self.y)))
    
  def __repr__(self):
    return str(self)
