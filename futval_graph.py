# futval_graph.py
# by Trey A. Sr. 12/12/2012
# updated the future value program to be graphical


from graphics import *

def main():
    # Introduction
    #print ("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    #principal = float(input("Enter the initial principal:"))
    #apr = float(input("Enter the annualized interest rate:"))

    #opens a input window
    
    win = GraphWin("input", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    Text(Point(1, 3), "initial principal:").draw(win)
    Text(Point(1, 1), "annualized interest:").draw(win)
    inputTextp = Entry(Point(2.25, 3), 5)
    inputTextp.draw(win)
    inputTexta = Entry(Point(2.25, 1), 5)
    inputTexta.draw(win)
    button = Text(Point(1.5, 2.0), "enter")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    win.getMouse()
    
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)
    
    # Draw bar for initial principal
    principal1 = inputTextp.getText()
    apr1 = inputTexta.getText()
    principal = float(principal1)
    apr = float(apr1)
    height = principal * 0.02
    bar = Rectangle (Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range (1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height ))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press to quit")
    win.close()

main()
