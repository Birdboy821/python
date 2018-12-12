#
#
#

from graphics import *
def main():
   win = GraphWin('DieDieDieDieDie', 2150, 500)

   dice1 = Rectangle(Point(150, 150), Point(400, 400))
   dice1.draw(win)
   dice2 = Rectangle(Point(550, 150), Point(800, 400))
   dice2.draw(win)
   dice3 = Rectangle(Point(950, 150), Point(1200, 400))
   dice3.draw(win)
   dice4 = Rectangle(Point(1350, 150), Point(1600, 400))
   dice4.draw(win)
   dice5 = Rectangle(Point(1750, 150), Point(2000, 400))
   dice5.draw(win)

   rad = 15
   dot11 = Circle(Point(275, 275), rad)
   dot11.draw(win)
   dot21 = Circle(Point(625, 325), rad)
   dot21.draw(win)
   dot22 = Circle(Point(725, 225), rad)
   dot22.draw(win)

main()
