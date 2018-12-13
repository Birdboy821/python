#CircleIntersection.py
#by christopher amell 12q-12-18
#to find the Circle Intersection thingy

#imports
from graphics import *
from math import *
def main():
   #inputs
   rad = eval(input('what is the radius of the circle '))
   #radius
   yint = eval(input('what is the y interset '))
   #the y interset
   
   win = GraphWin('Circle Intersection')
   win.setCoords(-10, -10, 10, 10)
   #window
   center = Point(0, 0)
   circle = Circle(center, rad)
   circle.draw(win)
   #circle
   line = Line(Point(-12, yint), Point(12, yint))
   line.draw(win)
   #line
   
   x = sqrt(rad ** 2 - yint ** 2) 
   i1 = Point(x, yint)
   i1.setFill('red')
   i1.draw(win)
   i2 = Point(-x , yint)
   i2.setFill('red')
   i2.draw(win)
   print(x,'and',-x)
main()
