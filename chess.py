#chess.py
#christopher amell 12-13-18
#game board for playing chess or checkers


from graphics import*
def main():
   win = GraphWin('chess board', 800, 800)

   win.setBackground('white')

   squareb1 = Rectangle(Point(0, 0),Point(100, 100))
   squareb1.setFill('black')
   squareb1.draw(win)

   squareb2 = Rectangle(Point(200, 0),Point(300, 100))
   squareb2.setFill('black')
   squareb2.draw(win)

   squareb3 = Rectangle(Point(400, 0),Point(500, 100))
   squareb3.setFill('black')
   squareb3.draw(win)

   squareb4 = Rectangle(Point(600, 0),Point(700, 100))
   squareb4.setFill('black')
   squareb4.draw(win)

   squareb5 = Rectangle(Point(100, 100),Point(200, 200))
   squareb5.setFill('black')
   squareb5.draw(win)

   squareb6 = Rectangle(Point(300, 100),Point(400, 200))
   squareb6.setFill('black')
   squareb6.draw(win)

   squareb7 = Rectangle(Point(500, 100),Point(600, 200))
   squareb7.setFill('black')
   squareb7.draw(win)

   squareb8 = Rectangle(Point(700, 100),Point(800, 200))
   squareb8.setFill('black')
   squareb8.draw(win)

   for i in range(4):
      squareb11 = squareb1.clone()
      squareb11.draw(win)
      squareb1.move(0, 200)

      squareb21 =squareb2.clone()
      squareb21.draw(win)
      squareb2.move(0, 200)

      squareb31= squareb3.clone()
      squareb31.draw(win)
      squareb3.move(0, 200)

      squareb41= squareb4.clone()
      squareb41.draw(win)
      squareb4.move(0, 200)

      squareb51= squareb5.clone()
      squareb51.draw(win)
      squareb5.move(0, 200)

      squareb61= squareb6.clone()
      squareb61.draw(win)
      squareb6.move(0, 200)

      squareb71= squareb7.clone()
      squareb71.draw(win)
      squareb7.move(0, 200)

      squareb81= squareb8.clone()
      squareb81.draw(win)
      squareb8.move(0, 200)
   
main()
