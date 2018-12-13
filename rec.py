#rec.py
#christopher amell 12-12-18
#This program displays information about a rectangle drawn by the user.

from graphics import *
from math import *
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

   rec = Rectangle(Point(c1x, c1y), Point(c2x, c2y))
   rec.draw(win)

   width = sqrt((c2x-c1x)**2 + (c1y-c1y)**2)
   print(width)

   length = sqrt((c1x-c1x)**2 + (c2y-c1y)**2)
   print(length)

   #area
   area = length * width
   print(area,'area')

   #perimeter
   perimeter = 2 * (length + width)
   print(perimeter,'perimeter')
main()
   
