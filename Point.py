class Point:
  x, y = 0, 0
  
  def __init__(self, _x = 0, _y = 0):
    self.x = _x
    self.y = _y
  
  def __str__ (self):
    return (str((self.x, self.y)))
    
  def __repr__(self):
    return str(self)
  
  def __mul__ (self, number):
    return Point(self.x * number, self.y * number)
    
  __rmul__ = __mul__
  
  def __add__ (self, other):
    return Point(self.x + other.x, self.y + other.y)
    
  def __eq__(self, other): 
    return self.__dict__ == other.__dict__


  def __lt__ (self, other):
    if ((self.x < other.x) or (self.y < other.y)):
      return True
    return False
  
  def __le__ (self, other):
    if ((self.x <= other.x) or (self.y <= other.y)):
      return True
    return False
    
  def __ne__ (self, other):
    if ((self.x != other.x) or (self.y != other.y)):
      return True
    return False
    
  def __gt__ (self, other):
    if ((self.x > other.x) or (self.y > other.y)):
      return True
    return False
  
  def __ge__ (self, other):
    if ((self.x >= other.x) or (self.y >= other.y)):
      return True
    return False
    
  
  