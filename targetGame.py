#targetGame.py
#by christopher amell
#to make a target

from graphics import *
def main():

   score = 0
   
   win = GraphWin('Target', 500, 500)
   center = Point(250, 250)
   circ4 = Circle(center, 225)
   circ4.setFill('white')
   circ4.draw(win)
   circ3 = Circle(center, 175)
   circ3.setFill('black')
   circ3.draw(win)
   circ2 = Circle(center, 125)
   circ2.setFill('blue')
   circ2.draw(win)
   circ1 = Circle(center, 75)
   circ1.setFill('red')
   circ1.draw(win)
   circ = Circle(center, 25)
   circ.setFill('yellow')
   circ.draw(win)

   for i in range(5):
      click1 = win.getMouse()
      c1x = click1.getX()
      c1y = click1.getY()
      arrow = Point(c1x, c1y)
      arrow.setFill('cyan4')
      arrow.draw(win)

      if 25 < c1x < 475 and 25 < c1y < 475:
         score +=1
         if 75 < c1x < 425 and 75 < c1y < 425:
            score += 2
            if 125 < c1x < 375 and 125 < c1y < 375:
               score += 2
               if 175 < c1x < 325 and 125 < c1y < 375:
                  score += 2
                  if 225 < c1x < 275 and 125 < c1y < 375:
                     score += 2
   print(score)
main()
