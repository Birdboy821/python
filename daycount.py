#dayCount.py
#christopher amell 1/14/2019
#a program that accepts a date as month/day/year, verifies that
#it is a valid date (see previous problem), and then calculates the corresponding day number

def main():
   date = input('what is your date (month/day/year): ')

   monthStr, dayStr, year = date.split("/")

   nv = 0
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

      if x == int(year): #leap year
         yn2 = 'l'  #leap year
         count == 0 #breaks the 1st loop
         break
      elif x == 4000: #not a leap year
         yn2 = 'n'    #not a leap year
         count == 0 #breaks the 1st loop
         break

   if yn1 == 'l' and yn2 == 'l':
      lp = 'yes'
   elif yn1 == 'n' or yn2 == 'n':
      lp = 'no'
   else:
      print('ERROR')

   if monthStr == '1': #jan
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
         
   elif monthStr == '2': #feb
      if int(dayStr) >= 30:
         print(date, "is not vaild")
         nv = 1
      else:
         print(date, "is vaild it's aleap year")
         
   elif monthStr == '3': #mar
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')

   elif monthStr == '4':#apr
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
      
   elif monthStr == '5': #may
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
         
   elif monthStr == '6': #jun
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
      
   elif monthStr == '7': #jul
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
         
   elif monthStr == '8': #aug
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
         
   elif monthStr == '9': #sep
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
      
   elif monthStr == '10': #oct
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
         
   elif monthStr == '11': #nov
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
      
   elif monthStr == '12': #dec
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
         nv = 1
      else:
         print(date, 'is vaild')
   else:
      print('done')

   if nv == 1:
      print("IT'S NOT VAILD YOU IDIOT")
   else:
      if int(monthStr) > 2 and lp == 'no':
         dayNum = 31 * (int(monthStr) - 1) + int(dayStr) - 4*(int(monthStr) + 23) // 10
      elif int(monthStr) > 2 and lp == 'yes':
         dayNum = (31 * (int(monthStr) - 1) + int(dayStr) - (4*(int(monthStr)) + 23) // 10) + 1
      else:
         dayNum = 31 * (int(monthStr) - 1) + int(dayStr)

   print(dayNum)
   
main()

