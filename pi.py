# pi.py
# by christopher amell
# a program that is for approximates the value of pi

def main():
   n = eval(input("how many terms do you want to summon "))
   x = n * 4
   y = 4
   o = 1
   for i in range(1, x, 4):
      y = y + 4/i - 4/o
      pie = y
      o = o + 2
      print(pie)
main()
