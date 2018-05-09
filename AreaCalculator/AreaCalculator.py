"""The purpose of this program is to prompt the user to select a shape, calculate the area of that shape, then print the results on the colsole."""

print "Welcome to the Area Calculator!"
print ""

option = raw_input("What shape would you like to calculate the area for?\nEnter C for Circle, or T for Triangle: ")

if (option == 'c' or option == 'C'):
  units = raw_input("Please enter the units of measure (cm, m, km): ")
  radius = float(raw_input("Please enter the radius of the circle: "))
  print "Calculating...."
  area = (3.14159 * (radius ** 2))
  print "Area of a circle with a radius of " + str(radius) + " " + units + " is: " + str(area) + " " + units
elif (option == 't' or option == 'T'):
  units = raw_input("Please enter the units of measure (cm, m, km): ")
  base = float(raw_input("Please enter the length of the base of the triangle: "))
  height = float(raw_input("Please enter the height of the triangle: "))
  print "Calculating...."
  area = (0.5 * base * height)
  print "Area of a triangle with the base of " + str(base) + " " + units + " and a height of " + str(height) + " " + units + " is: " + str(area) + " " + units
else:
  print "You have entered an invalid shape option."
  
print "\nThank you for using AreaCalculator!\nExiting..."
