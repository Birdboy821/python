#leapYear.py
#christopher amell 1/14/19
#a program that calculates whether a year is a leap year

def main():
   year = eval(input('what is your year: '))
   x = 0         #counting vaule for the 4s rule
   y = 0         #counting vaule for the 400s rule
   count = 1     #while loop 2nd
   count2 = 1    #while loop 2nd

   
   while(count2 == 1):   #400s rule
      y += 400
      if y == year: #leap year
         yn1 = 'l'  #leap year
         count2 == 0 #breaks the 2nd loop
         break
      elif year == 100 or year == 200 or year == 300 or year == 500 or year == 600 or year == 700 or year == 900 or year == 1000 or year == 1100 or year == 1300 or year == 1400 or year == 1500 or year == 1600 or year == 1700 or year == 1800 or year == 1900 or year == 2100 or year == 2200 or year == 2300:
 #not a leap year ^
         yn1 = 'n' #not a leap year
         break
      elif y == 2400: #pass through
         yn1 = 'l'    #pass through
         count2 == 0 #breaks the 2nd loop
         break
   while(count == 1):   #4s rule
      x += 4

      if x == year: #leap year
         yn2 = 'l'  #leap year
         count == 0 #breaks the 1st loop
         break
      elif x == 4000: #not a leap year
         yn2 = 'n'    #not a leap year
         count == 0 #breaks the 1st loop
         break

   if yn1 == 'l' and yn2 == 'l':
      print("It's a leap year")
   elif yn1 == 'n' or yn2 == 'n':
      print("It's not a leap year")
   else:
      print('ERROR')
main()
