#lineDes.py
#christopher amell 12-12-18
#This program allows the user to draw a line segment and
#then displays some graphical and textual information about the line segment.

#FIXED: undefindded slope is no long there

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

   #print(c1x, c1y)
   #print(c2x, c2y)

   #draws lin
   line = Line(Point(c1x, c1y), Point(c2x, c2y))
   line.draw(win)
   #finds and draws mid point
   midX = ((c1x+c2x)/2)
   midY = ((c1y+c2y)/2)
   mid = Point(midX, midY)
   mid.setFill('cyan')
   mid.draw(win)
   print(midX, midY)

   X = c2x - c1x
   Y = c2y - c1y
   if Y == 0:
      print('ERROR')
   else:
      slope = sqrt(X**2 / Y**2)
      print(slope)
main()
