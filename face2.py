#face2.py
#by christopher amell 1/3/19
#to make a face (*7*)

from graphics import *
def face(center, size, win):
   cen = list(center)
   sizeAct = size
   eyrcen = Point(cen[0] - 30, cen[1] + 20)
   eylcen = Point(cen[0] + 30, cen[1] + 20)
   noscen = Point(cen[0] , cen[1])
   moth = Circle(Point(cen[0], cen[1] - 25), 20)
   eyr = Circle(eyrcen , 10 + sizeAct/25)
   eyl = Circle(eylcen , 10 + sizeAct/25)
   nos = Circle(noscen , 5 + sizeAct/25)
   eyr.setFill('white')
   eyl.setFill('white')
   nos.setFill('blue')
   eyr.draw(win)
   eyl.draw(win)
   nos.draw(win)
   moth.draw(win)

def main():
   win = GraphWin('face', 1000, 1000)
   win.setCoords(-500, -500, 500, 500)
   picht = input('')
   for i in range(10):
      click1 = win.getMouse()
      c1x = click1.getX()
      c1y = click1.getY()
      center = c1x, c1y

      click2 = win.getMouse()
      c2x = click2.getX()
      c2y = click2.getY()
      size = (c2x + c2y) / 2

      face(center, size, win)
   
main()
