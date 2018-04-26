from Point import Point

def mkcode(point1, xmin, xmax, ymin, ymax):
  firstBit = bin(ymax - point1.y)[0]
  secondBit = bin(point1.y - ymin)[0]
  thirdBit = bin(xmax - point1.x)[0]
  fourthBit = bin(point1.x - xmin)[0]
  
  bits = ""
  
  for bit in firstBit + secondBit + thirdBit + fourthBit:
    if bit == "-":
      bits = bits + "1"
    else:
      bits = bits + bit
      
  return bits

def cohenSutherland(point1, point2, xmin, xmax, ymin, ymax):
  return mkcode(point1, xmin, xmax, ymin, ymax)