#diediediediedie.py
#christopher amell by 12/11/18
#displays 1-5 in dice

from graphics import *
def main():
   win = GraphWin('diediediediedie')

   #dice 1
   dice1 = Rectangle(Point(11, 11), Point(20, 20))
   dot11 = Point(15, 15)
   dice1.draw(win)
   dot11.draw(win)

   #dice 2
   dice2 = Rectangle(Point(26, 11), Point(35, 20))
   dot21 = Point(28, 13)
   dot22 = Point(32, 17)
   dice2.draw(win)
   dot21.draw(win)
   dot22.draw(win)

   #dice 3
   dice3 = Rectangle(Point(41, 11), Point(50 ,20))
   dot31 = Point(45, 15)
   dot32 = Point(47, 17)
   dot33 = Point(43, 13)
   dice3.draw(win)
   dot31.draw(win)
   dot32.draw(win)
   dot33.draw(win)

   #dice 4
   dice4 = Rectangle(Point(56, 11), Point(65, 20))
   dot41 = Point(58, 17)
   dot42 = Point(62, 17)
   dot43 = Point(58, 13)
   dot44 = Point(62, 13)
   dice4.draw(win)
   dot41.draw(win)
   dot42.draw(win)
   dot43.draw(win)
   dot44.draw(win)

   #dice 5
   dice5 = Rectangle(Point(71, 11), Point(80, 20))
   dot51 = Point(75, 15)
   dot52 = Point(77, 13)
   dot53 = Point(77, 17)
   dot54 = Point(73, 13)
   dot55 = Point(73, 17)
   dice5.draw(win)
   dot51.draw(win)
   dot52.draw(win)
   dot53.draw(win)
   dot54.draw(win)
   dot55.draw(win)
main()
