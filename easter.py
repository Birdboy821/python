#easter.py
#1/14/19 christopher amell
#A formula for computing Easter in the years 1982-2048

def main():
   year = eval(input('what is your year: '))
   if 1982 <= year <= 2048:
      a = year % 19 
      b = year % 4
      c = year % 7
      d = (19*a + 24) % 30
      e = (2*b + 4*c + 6*d + 5) % 7
      day = int(22 + d + e)

      if day > 31:
         day = day - 31
         print('April', day, year)
      else:
         print('March', day, year)
main()

