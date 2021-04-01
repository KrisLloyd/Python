"""The purpose of this program is to prompt the user to select a shape, calculate the area of that shape, then print the results on the colsole."""

def units():
  while True:
      units = input("Please enter the units of measure (cm, m, km, ( 'x' to exit)): ")
      if units.lower() in ['cm', 'm', 'km', 'x']:
        if units.lower() == 'x':
          return -1
        break
  return units.lower()

def getNum(s):
  while True:
      num = input(s)
      if num.lower() == 'x':
        return -1
      if num.isnumeric() and float(num) > 0:
        num = float(num)
        break
  return num

def shape():
  # Determine which shape
  while True:
    print("What shape would you like to calculate the area for?")
    option = input("[c] - Circle\n[r] - Rectangle\n[s] - Square\n[t] - Triangle\n[x] - Exit: ")
    if option.lower() in ['c', 'r', 's', 't', 'x']:
      if option.lower() == 'x':
        return -1
      break
  
  # Circle
  if option.lower() == 'c':
    unit = units()
    if unit == -1:
      return unit
    radius = getNum("Please enter the radius of the circle ('x' to exit): ")
    if radius == -1:
      return radius
    area = 3.14159 * (radius ** 2)
    return "Circle with radius {radius:.2f}{units} has an area of {area:.2f}{units}\u00b2".format(radius = radius, units = unit, area = area)
  elif option.lower() == 's': 
    # Square
    unit = units()
    if unit == -1:
      return unit
    side = getNum("Please enter the length of one side ('x' to exit): ")
    if side == -1:
      return side
    area = side**2
    return "Square with side length {side:.2f}{units} has an area of {area:.2f}{units}\u00b2".format(side = side, units = unit, area = area)
  elif option.lower() == 'r': 
    # Rectangle
    unit = units()
    if unit == -1:
      return unit
    length = getNum("Please enter the length of the rectangle ('x' to exit): ")
    if length == -1:
      return length
    width = getNum("Please enter the width of the rectangle ('x' to exit): ")
    if width == -1:
      return width
    area = length * width
    return "Rectangle with side length {length:.2f}{units} and width length {width:.2f}{units} has an area of {area:.2f}{units}\u00b2".format(length = length, width = width, units = unit, area = area)
  else:
    # Triangle
    unit = units()
    if unit == -1:
      return unit
    base = getNum("Please enter the length of the base of the triangle ('x' to exit): ")
    if base == -1:
      return base
    height = getNum("Please enter the height of the triangle ('x' to exit): ")
    if height == -1:
      return height
    area = (0.5 * base * height)
    return "Triangle with the base of {base:.2f}{units} and a height of {height:.2f}{units} has an area of {area}{units}\u00b2".format(base = base, units = unit, height = height, area = area)
  

if __name__ == "__main__":
  print(shape())
