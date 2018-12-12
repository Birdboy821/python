#some.py
#by christopher amell
#moves square around

from graphics import *

def main():
   win = GraphWin()
   shape = Rectangle(Point(50, 50), Point(20, 20))
   shape.setOutline("red")
   shape.setFill("red")
   shape.draw(win)
   for i in range(10):
      shape1 = shape.clone()
      shape1.draw(win)
      p = win.getMouse()
      c = shape.getCenter()
      dx = p.getX() - c.getX()
      dy = p.getY() - c.getY()
      shape.move(dx,dy)
   center = Point(100, 100)
   label = Text(center, "Click again to quit")
   label.draw(win)
   win.getMouse()
   win.close()
main()
