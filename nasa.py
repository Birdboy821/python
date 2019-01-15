#nasa.py
#christopher amell 1/15/2019
#a program which prompts for three different numbers,
#as a simulation of three different computational results

from random import *

def main():
   y = randint(0, 2)
   x = randint(0, 2)
   z = randint(1, 3)
   one = x - y + z
   two = x * y / z
   three = x + y - z

   if one == two or two == three or three == one:
      print('match')
   else:
      print('ERROR')

   print(one, two, three)
   
main()
   
