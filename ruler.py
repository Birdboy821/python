#ruler.py
#christopher amell 12-13-18
# a 12" ruler on the screen


from graphics import *
def main():
   win = GraphWin('BirdRuler', 1153, 100)

   inch1 = Line(Point(0, 30), Point(0, 0))
   inch1.draw(win)
   inch12 = Line(Point(48, 15), Point(48, 0))
   inch14 = Line(Point(24, 10), Point(24, 0))
   inch144 = Line(Point(72, 10), Point(72, 0))

   #number
   a1 = Text(Point( 0, 30), 0 ).draw(win)
   a1 = Text(Point( 96, 30), 1 ).draw(win)
   a2 = Text(Point( 192, 30), 2 ).draw(win)
   a3 = Text(Point( 288, 30), 3 ).draw(win)
   a4 = Text(Point( 384, 30), 4 ).draw(win)
   a5 = Text(Point( 480, 30), 5 ).draw(win)
   a6 = Text(Point( 576, 30), 6 ).draw(win)
   a7 = Text(Point( 672, 30), 7 ).draw(win)
   a8 = Text(Point( 768, 30), 8 ).draw(win)
   a9 = Text(Point( 864, 30), 9 ).draw(win)
   a10 = Text(Point( 960, 30), 10 ).draw(win)
   a11 = Text(Point( 1056, 30), 11 ).draw(win)
   a12 = Text(Point( 1152, 30), 12 ).draw(win)
   
   for i in range(12):
      inch2 = inch1.clone()
      inch2.draw(win)
      inch1.move(96, 0)
      inch22 = inch12.clone()
      inch22.draw(win)
      inch12.move(96, 0)
      inch24 = inch14.clone()
      inch24.draw(win)
      inch14.move(96, 0)
      inch244 = inch144.clone()
      inch244.draw(win)
      inch144.move(96, 0)

main()
