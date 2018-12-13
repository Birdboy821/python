#graphpaper.py
#christopher amell 12-13-18
#standard four-quadrant coordinate graph paper

from graphics import *
def main():
   win = GraphWin('graphy', 1000,1000)
   win.setCoords(-1000, -1000, 1000, 1000)
   center = Point(0, 0)
## axises
   xaxis = Line(Point(-8000, 0), Point(8000, 0))
   xaxis.draw(win)
   yaxis = Line(Point(0, -8000), Point(0, 8000))
   yaxis.draw(win)

## dashes
   liney1 = Line(Point(10, -999), Point(-10,-999))
   liney1.draw(win)
   linex1 = Line(Point(-999, 10), Point(-999, -10))
   linex1.draw(win)
   #the x axis numbers
   axisx = Text(Point( 999 , -15), 20 ).draw(win)
   axisx = Text(Point( 949 , -15), 19 ).draw(win)
   axisx = Text(Point( 899 , -15), 18 ).draw(win)
   axisx = Text(Point( 849 , -15), 17 ).draw(win)
   axisx = Text(Point( 799 , -15), 16 ).draw(win)
   axisx = Text(Point( 749 , -15), 15 ).draw(win)
   axisx = Text(Point( 699 , -15), 14 ).draw(win)
   axisx = Text(Point( 649 , -15), 13 ).draw(win)
   axisx = Text(Point( 599 , -15), 12 ).draw(win)
   axisx = Text(Point( 549 , -15), 11 ).draw(win)
   axisx = Text(Point( 499 , -15), 10 ).draw(win)
   axisx = Text(Point( 449 , -15), 9 ).draw(win)
   axisx = Text(Point( 399 , -15), 8 ).draw(win)
   axisx = Text(Point( 349 , -15), 7 ).draw(win)
   axisx = Text(Point( 299 , -15), 6 ).draw(win)
   axisx = Text(Point( 249 , -15), 5 ).draw(win)
   axisx = Text(Point( 199 , -15), 4 ).draw(win)
   axisx = Text(Point( 149 , -15), 3 ).draw(win)
   axisx = Text(Point( 99 , -15), 2 ).draw(win)
   axisx = Text(Point( 49 , -15), 1 ).draw(win)
   axisx = Text(Point( 0 , -15), 0 ).draw(win)
   axisx = Text(Point(-49 , -15),-1 ).draw(win)
   axisx = Text(Point(-99 , -15),-2 ).draw(win)
   axisx = Text(Point(-149 , -15),-3 ).draw(win)
   axisx = Text(Point(-199 , -15),-4 ).draw(win)
   axisx = Text(Point(-249 , -15),-5 ).draw(win)
   axisx = Text(Point(-299 , -15),-6 ).draw(win)
   axisx = Text(Point(-349 , -15),-7 ).draw(win)
   axisx = Text(Point(-399 , -15),-8 ).draw(win)
   axisx = Text(Point(-449 , -15),-9 ).draw(win)
   axisx = Text(Point(-499 , -15),-10 ).draw(win)
   axisx = Text(Point(-549 , -15),-11 ).draw(win)
   axisx = Text(Point(-599 , -15),-12 ).draw(win)
   axisx = Text(Point(-649 , -15),-13 ).draw(win)
   axisx = Text(Point(-699 , -15),-14 ).draw(win)
   axisx = Text(Point(-749 , -15),-15 ).draw(win)
   axisx = Text(Point(-799 , -15),-16 ).draw(win)
   axisx = Text(Point(-849 , -15),-17 ).draw(win)
   axisx = Text(Point(-899 , -15),-18 ).draw(win)
   axisx = Text(Point(-949 , -15),-19 ).draw(win)
   axisx = Text(Point(-999 , -15),-20 ).draw(win)

   #the y numbers
   axisy = Text(Point( -15, 999), 20 ).draw(win)
   axisy = Text(Point( -15, 949), 19 ).draw(win)
   axisy = Text(Point( -15, 899), 18 ).draw(win)
   axisy = Text(Point( -15, 849), 17 ).draw(win)
   axisy = Text(Point( -15, 799), 16 ).draw(win)
   axisy = Text(Point( -15, 749), 15 ).draw(win)
   axisy = Text(Point( -15, 699), 14 ).draw(win)
   axisy = Text(Point( -15, 649), 13 ).draw(win)
   axisy = Text(Point( -15, 599), 12 ).draw(win)
   axisy = Text(Point( -15, 549), 11 ).draw(win)
   axisy = Text(Point( -15, 499), 10 ).draw(win)
   axisy = Text(Point( -15, 449), 9 ).draw(win)
   axisy = Text(Point( -15, 399), 8 ).draw(win)
   axisy = Text(Point( -15, 349), 7 ).draw(win)
   axisy = Text(Point( -15, 299), 6 ).draw(win)
   axisy = Text(Point( -15, 249), 5 ).draw(win)
   axisy = Text(Point( -15, 199), 4 ).draw(win)
   axisy = Text(Point( -15, 149), 3 ).draw(win)
   axisy = Text(Point( -15, 99 ), 2 ).draw(win)
   axisy = Text(Point( -15, 49 ), 1 ).draw(win)
   axisy = Text(Point( -15, 0 ), 0 ).draw(win)
   axisy = Text(Point( -15, -49),-1 ).draw(win)
   axisy = Text(Point( -15, -99),-2 ).draw(win)
   axisy = Text(Point( -15, -149),-3 ).draw(win)
   axisy = Text(Point( -15, -199),-4 ).draw(win)
   axisy = Text(Point( -15, -249),-5 ).draw(win)
   axisy = Text(Point( -15, -299),-6 ).draw(win)
   axisy = Text(Point( -15, -349),-7 ).draw(win)
   axisy = Text(Point( -15, -399),-8 ).draw(win)
   axisy = Text(Point( -15, -449),-9 ).draw(win)
   axisy = Text(Point( -15, -499),-10 ).draw(win)
   axisy = Text(Point( -15, -549),-11 ).draw(win)
   axisy = Text(Point( -15, -599),-12 ).draw(win)
   axisy = Text(Point( -15, -649),-13 ).draw(win)
   axisy = Text(Point( -15, -699),-14 ).draw(win)
   axisy = Text(Point( -15, -749),-15 ).draw(win)
   axisy = Text(Point( -15, -799),-16 ).draw(win)
   axisy = Text(Point( -15, -849),-17 ).draw(win)
   axisy = Text(Point( -15, -899),-18 ).draw(win)
   axisy = Text(Point( -15, -949),-19 ).draw(win)
   axisy = Text(Point( -15, -999),-20 ).draw(win)

   for i in range(42):
      liney2 = liney1.clone()
      liney2.draw(win)
      liney1.move(0, 50)
      linex2 = linex1.clone()
      linex2.draw(win)
      linex1.move(50, 0)

main()