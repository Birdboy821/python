#ruler.py
#christopher amell 12-13-18 modifididididididididididi 12-13-18
# a 12" ruler on the screen added mimimeter and centimeter


from graphics import *
def main():
   win = GraphWin('BirdRuler', 1153, 100)

   inch1 = Line(Point(0, 30), Point(0, 0))
   inch1.draw(win)
   inch12 = Line(Point(48, 15), Point(48, 0))
   inch14 = Line(Point(24, 10), Point(24, 0))
   inch144 = Line(Point(72, 10), Point(72, 0))

   #number
   a0 = Text(Point( 0, 30), 0 ).draw(win)
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

   mm1 = Line(Point(0, 90), Point(0, 100)).draw(win)

   cm1 = Line(Point(0, 70), Point(0, 100)).draw(win)

   b0 = Text(Point( 0, 70), 0 ).draw(win)
   b1 = Text(Point( 40, 70), 1 ).draw(win)
   b2 = Text(Point( 80, 70), 2 ).draw(win)
   b3 = Text(Point( 120, 70), 3 ).draw(win)
   b4 = Text(Point( 160, 70), 4 ).draw(win)
   b5 = Text(Point( 200, 70), 5 ).draw(win)
   b6 = Text(Point( 240, 70), 6 ).draw(win)
   b7 = Text(Point( 280, 70), 7 ).draw(win)
   b8 = Text(Point( 320, 70), 8 ).draw(win)
   b9 = Text(Point( 360, 70), 9 ).draw(win)
   b10 = Text(Point( 400, 70), 10 ).draw(win)
   b11 = Text(Point( 440, 70), 11 ).draw(win)
   b12 = Text(Point( 480, 70), 12 ).draw(win)
   b13 = Text(Point( 520, 70), 13 ).draw(win)
   b14 = Text(Point( 560, 70), 14 ).draw(win)
   b15 = Text(Point( 600, 70), 15 ).draw(win)
   b16 = Text(Point( 640, 70), 16 ).draw(win)
   b17 = Text(Point( 680, 70), 17 ).draw(win)
   b18 = Text(Point( 720, 70), 18 ).draw(win)
   b19 = Text(Point( 760, 70), 19 ).draw(win)
   b20 = Text(Point( 800, 70), 20 ).draw(win)
   b21 = Text(Point( 840, 70), 21 ).draw(win)
   b22 = Text(Point( 880, 70), 22 ).draw(win)
   b23 = Text(Point( 920, 70), 23 ).draw(win)
   b24 = Text(Point( 960, 70), 24 ).draw(win)
   b25 = Text(Point( 1000, 70), 25 ).draw(win)
   b26 = Text(Point( 1040, 70), 26 ).draw(win)
   b27 = Text(Point( 1080, 70), 27 ).draw(win)
   b28 = Text(Point( 1120, 70), 28 ).draw(win)
   
   
   for i in range(1200):
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

      mm2 = mm1.clone()
      mm2.draw(win)
      mm1.move(4, 0)

      cm2 = cm1.clone()
      cm2.draw(win)
      cm1.move(40, 0)

main()

