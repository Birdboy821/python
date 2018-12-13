#flag.py
#christopher amell 12-13-18
#a canadian flag

from graphics import *
def main():
   win = GraphWin('graphy', 640,320)
   win.setBackground("white")

   #canadian back ground
   left = Rectangle(Point(0,0),Point(160, 320))
   left.draw(win)
   right = Rectangle(Point(480,0),Point(640, 320))
   right.draw(win)
   left.setFill('red')
   right.setFill('red')
   left.setOutline('red')
   right.setOutline('red')

   #maple leaf shape
   center = Polygon(Point(320, 60), Point(240, 200), Point(400, 200))
   center.draw(win)
   top1 = Polygon(Point(280, 50), Point(320, 160), Point(320, 60))
   top1.draw(win)
   top2 = Polygon(Point(360, 50), Point(320, 160), Point(320, 60))
   top2.draw(win)
   top3 = Polygon(Point(320, 25), Point(340, 60), Point(300, 60))
   top3.draw(win)
   sidel1 = Polygon(Point(200, 160), Point(240, 100), Point(320, 160), Point(280,200))
   sidel1.draw(win)
   sidel2 = Polygon(Point(210, 145), Point(180, 110), Point(230, 120))
   sidel2.draw(win)
   sider1 = Polygon(Point(440, 160), Point(400, 100), Point(320, 160), Point(360,200))
   sider1.draw(win)
   sider2 = Polygon(Point(430, 145), Point(460, 110), Point(410, 120))
   sider2.draw(win)
   stem = Rectangle(Point(315, 200), Point(325, 280))
   stem.draw(win)

   #maple leaf color
   center.setFill('red')
   top1.setFill('red')
   top2.setFill('red')
   top3.setFill('red')
   sidel1.setFill('red')
   sidel2.setFill('red')
   sider1.setFill('red')
   sider2.setFill('red')
   stem.setFill('red')
   center.setOutline('red')
   top1.setOutline('red')
   top2.setOutline('red')
   top3.setOutline('red')
   sidel1.setOutline('red')
   sidel2.setOutline('red')
   sider1.setOutline('red')
   sider2.setOutline('red')
   stem.setOutline('red')

##O Canada!
##Our home and native land!
##True patriot love in all of us command.
##With glowing hearts we see thee rise,
##The True North strong and free!
##From far and wide,
##O Canada, we stand on guard for thee.
##God keep our land glorious and free!
##O Canada, we stand on guard for thee.
##O Canada, we stand on guard for thee.
main()
