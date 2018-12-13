#tri.py
#christopher12-12-18
#three clicks for the vertices of a triangle

from math import *
from graphics import *
def main():
   win = GraphWin('line', 500, 500)
   #first click
   click1 = win.getMouse()
   c1x = click1.getX()
   c1y = click1.getY()
   #second click
   click2 = win.getMouse()
   c2x = click2.getX()
   c2y = click2.getY()
   #third click
   click3 = win.getMouse()
   c3x = click3.getX()
   c3y = click3.getY()

   tri = Polygon(Point(c1x, c1y), Point(c2x, c2y), Point(c3x, c3y))
   tri.draw(win)

   side1 = sqrt((c2x-c1x)**2 + (c2y-c1y)**2)
   side2 = sqrt((c3x-c2x)**2 + (c3y-c2y)**2)
   side3 = sqrt((c1x-c3x)**2 + (c1y-c3y)**2)

   perimeter = side1 + side2 +side3

   s = (side1 + side2 + side3) / 2
   area = sqrt(s * (s-side1)*(s-side2)*(s-side3))

   print(perimeter, area, side1, side2, side3)
main()
