# File: chaos.py
# Created 2/12/15 by Kevin Grimsley
# A simple program illustrating chaotic behavior.

def main():
    #n = eval(input("How many numbers should I print? "))
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100) :
        x = 3.9 * x * (1 - x)
        print(x)
main()
