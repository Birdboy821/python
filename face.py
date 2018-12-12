#face.py
#by christopher amell
#to make a face (*7*)

from graphics import *
def main():
   win = GraphWin('face')
   eyrcen = Point(70, 80)
   eylcen = Point(130, 80)
   noscen = Point(100, 100)
   moth = Oval(Point(70, 110), Point(130, 140))
   eyr = Circle(eyrcen, 10)
   eyl = Circle(eylcen, 10)
   nos = Circle(noscen, 5)
   eyr.setFill('white')
   eyl.setFill('white')
   nos.setFill('blue')
   eyr.draw(win)
   eyl.draw(win)
   nos.draw(win)
   moth.draw(win)
main()
