#moveTo.py
#christopher amell 1/4/19
# a program that draws a circle
#and then allows the user to click the window 10 times

from graphics import *

def moveTo(shape, newCenter):
   shape.move(newCenter[0], newCenter[1])




def main():
   win = GraphWin()
   shape = Circle(Point(100, 100), 10)
   shape.setOutline('gold')
   shape.setFill('yellow')
   shape.draw(win)
   for i in range(10):
      p = win.getMouse()
      c = shape.getCenter()
      dx = p.getX() - c.getX()
      dy = p.getY() - c.getY()
      newCenter = dx, dy
      moveTo(shape, newCenter)
main()
