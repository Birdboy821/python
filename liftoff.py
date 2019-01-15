#liftoff.py
#christopher amell 1/4/19
# simulate a launch countdown,
#starting from 10 and counting down to 1, followed by the word “LIFTOFF !!”

from time import *

def countdown():
   x = 10
   for i in range(x):
      print(x)
      sleep(1)
      x -= 1

def main():
   countdown()
   print('LIFTOFF!!')
main()
