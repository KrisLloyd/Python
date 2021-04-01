[< Back to Python Projects](https://github.com/KrisLloyd/Python#python)
***

# About
Program that prompts the user for a type of shape and values and returns the area of that shape.

# Useage

```python
import AreaCalculator

# Call the shape() function to bring up the interactive menu
shape()
```

The program allows for the area calculation of the following shapes:
* Square
* Rectangle
* Triangle
* Circle

Escape value of **'x'** has been incorporated into user prompts. Program will return **-1**.

# Examples

* Area of a circle with radius of 5m:

  ```
  What shape would you like to calculate the area for?
  [c] - Circle
  [r] - Rectangle
  [s] - Square
  [t] - Triangle
  [x] - Exit: c
  Please enter the units of measure (cm, m, km, ( 'x' to exit)): m
  Please enter the radius of the circle ('x' to exit): 5
  Circle with radius 5.00m has an area of 78.54m²
  ```

* Area of a triangle with base of 3cm and height of 6cm:

  ```
  What shape would you like to calculate the area for?
  [c] - Circle
  [r] - Rectangle
  [s] - Square
  [t] - Triangle
  [x] - Exit: t
  Please enter the units of measure (cm, m, km, ( 'x' to exit)): cm
  Please enter the length of the base of the triangle ('x' to exit): 3
  Please enter the height of the triangle ('x' to exit): 6
  Triangle with the base of 3.00cm and a height of 6.00cm has an area of 9.0cm²
  ```

* Graceful exit with code **-1** during operation:

  ```
  What shape would you like to calculate the area for?
  [c] - Circle
  [r] - Rectangle
  [s] - Square
  [t] - Triangle
  [x] - Exit: s
  Please enter the units of measure (cm, m, km, ( 'x' to exit)): km
  Please enter the length of one side ('x' to exit): x
  -1
  ```
