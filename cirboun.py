#cirboun.py
#christopher amell 1/15/2019
#a program to animate a circle bouncing around a window

from graphics import *
from time import *
from random import *

def main():
   win = GraphWin('movement', 500, 500)
   circ = Circle(Point(250, 250), 25)
   circ.setFill('yellow')
   circ.draw(win)

   count = 1
   directionX = 10
   directionY = 10
   zy = 250

   while count == 1:
      x = randint(1, 4)
      update(30)
      circ.move(directionX, directionY/x)
      z = circ.getCenter()
      zx = z.getX()
      zy = z.getY()
      
      if zx >= 500 or zx <= 0:
         directionX *= -1
         print('if')

      if zy >= 500 or zy <= 0:
         directionY *= -1
         print('if')

      else:
         print(zx, zy, directionY/x)
main()
