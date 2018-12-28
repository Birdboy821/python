#exam.py
#christopher amell 12/27/18
#plot a horizontal bar chart of student exam scores

#imports
from graphics import *

def main():
    file = open('examInput.txt', 'r')

    students = file.readline()
    z = int(students.split(':')[1])
    y = z*23
    file.readline()
    file.readline()
    x = 1
    win = GraphWin('Exam Output', 400, y)
    for i in range(z):
        w = file.readline()
        name = w.split(';')
        xs = x * 20
        grade = Rectangle(Point(0, xs), Point(int(name[1])*4, xs+20))
        grade.setFill('gold')
        grade.draw(win)
        Text(Point( 35, xs+10), name[0]).draw(win)
        x += 1

    
main()
