#target.py
#by christopher amell
#to make a target

from graphics import *
def main():
   win = GraphWin('Target')
   center = Point(100, 100)
   circ4 = Circle(center, 50)
   circ4.setFill('white')
   circ4.draw(win)
   circ3 = Circle(center, 40)
   circ3.setFill('black')
   circ3.draw(win)
   circ2 = Circle(center, 30)
   circ2.setFill('blue')
   circ2.draw(win)
   circ1 = Circle(center, 20)
   circ1.setFill('red')
   circ1.draw(win)
   circ = Circle(center, 10)
   circ.setFill('yellow')
   circ.draw(win)
main()
