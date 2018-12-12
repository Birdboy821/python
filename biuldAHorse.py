#biuldAHorse.py
#christopher amell 12-11-2018
#builds a house with five clicks

from graphics import *
from math import *

def main():
   win = GraphWin('build a horse', 500, 500)

   click1 = win.getMouse()
   c1x = click1.getX()
   c1y = click1.getY()
##   print(c1x, c1y)
   
   click2 = win.getMouse()
   c2x = click2.getX()
   c2y = click2.getY()
##   print(c2x, c2y)

   house = Rectangle(Point(c1x, c1y), Point(c2x, c2y))
   house.draw(win)

   bl = sqrt((c1x - c1x) ** 2 + (c1y - c2y) ** 2 )
   fifth = bl / 5
   mid = fifth / 2

##   print(bl ,"and", fifth)
   
   click3 = win.getMouse()
   c3x = click3.getX()
   c3y = click3.getY()

   doorL = c3x - mid
   doorR = c3x + mid
   
   door = Rectangle(Point(doorL, c3y), Point(doorR, c1y))

   door.draw(win)

   click4 = win.getMouse()
   c4x = click4.getX()
   c4y = click4.getY()
   e = mid + c4x
   n = mid + c4y
   w = c4x - mid
   s = c4y - mid

   winddoor = Rectangle(Point(n, e), Point(s, w))

   winddoor.draw(win)

   click5 = win.getMouse()
   c5x = click5.getX()
   c5y = click5.getY()

   roof = Polygon(Point(c2x, c2y), Point(c1x, c2y), Point(c5x, c5y))
   roof.draw(win)
main()
