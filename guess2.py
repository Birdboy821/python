# guess2.py
# by christopher amell
# a program that is for making a guess of a square root


def nextGuess(guess, n):
   p=(guess+(n/guess))/2
   m = str(n)
   print(p ,'is about the square root of '+ m + '.')
   
def main():
   n = eval(input("what number do you want to find to square root of "))
   guess = eval(input("What is your guess "))
   nextGuess(guess, n)
main()
