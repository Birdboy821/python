#histogram.py
#christopher amell 12/27/18
#draw a quiz score histogram.

#imports
from graphics import *

def main():
    file = open('histogram.txt', 'r')
    sfile = open('histogram.txt', 'r')

    file.readline()

    z = sfile.readlines()
    x = -1
    t = 0
    win = GraphWin('Exam Output', 460, 200)
    for i in z:
        x += 1
    #print(x , z)

    

    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myList = [ ]
    number = Rectangle(Point(20,170),Point(40,150)).draw(win)
    text0 = Text(Point(30, 180), 0).draw(win)
    text1 = Text(Point(70, 180), 1).draw(win)
    text2 = Text(Point(110, 180), 2).draw(win)
    text3 = Text(Point(150, 180), 3).draw(win)
    text4 = Text(Point(190, 180), 4).draw(win)
    text5 = Text(Point(230, 180), 5).draw(win)
    text6 = Text(Point(270, 180), 6).draw(win)
    text7 = Text(Point(310, 180), 7).draw(win)
    text8 = Text(Point(350, 180), 8).draw(win)
    text9 = Text(Point(390, 180), 9).draw(win)
    text10 = Text(Point(430, 180), 10).draw(win)
    for r in range(10):
        number2 = number.clone()
        number2.draw(win)
        number.move(40, 0)
    bottem = Rectangle(Point(0, 170),Point(500, 155))
    bottem.setFill('cyan')
    bottem.draw(win)
    
        
    q0 = 130
    q1 = 130
    q2 = 130
    q3 = 130
    q4 = 130
    q5 = 130
    q6 = 130
    q7 = 130
    q8 = 130
    q9 = 130
    q10 = 130
    for a in range(x):
        
        d = int(file.readline())
        if d == 0:
            place = Rectangle(Point(20,q0),Point(40,150)).draw(win)
            q0 -= 20
        else:
            if d==1:
                place = Rectangle(Point(60,q1),Point(80,150)).draw(win)
                q1 = q1 - 20
            else:
                if d==2:
                    place = Rectangle(Point(100,q2),Point(120,150)).draw(win)
                    q2 -= 20
                else:
                    if d==3:
                        place = Rectangle(Point(140,q3),Point(160,150)).draw(win)
                        q3 -= 20
                    else:
                        if d==4:
                            place = Rectangle(Point(180,q4),Point(200,150)).draw(win)
                            q4 -= 20
                        else:
                            if d==5:
                                place = Rectangle(Point(220,q5),Point(240,150)).draw(win)
                                q5 -= 20
                            else:
                                if d==6:
                                    place = Rectangle(Point(260,q6),Point(280,150)).draw(win)
                                    q6 -= 20
                                else:
                                    if d==7:
                                        place = Rectangle(Point(300,q7),Point(320,150)).draw(win)
                                        q7 -= 20
                                    else:
                                        if d==8:
                                            place = Rectangle(Point(340,q8),Point(360,150)).draw(win)
                                            q8 -= 20
                                        else:
                                            if d==9:
                                                place = Rectangle(Point(380,q9),Point(400,150)).draw(win)
                                                q9 -= 20
                                            else:
                                                place = Rectangle(Point(420,q10),Point(440,150)).draw(win)
                                                q10 -= 20
            
    file.close
    sfile.close
main()
