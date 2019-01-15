#dateCheck.py
#christopher amell 1/14/2019
#a program that accepts a date in the
#form month/day/year and outputs whether or not the date is valid

def main():
   date = input('what is your date (month/day/year): ')

   monthStr, dayStr, yearStr = date.split("/")

   if monthStr == '1': #jan
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
         
   elif monthStr == '2': #feb
      if int(dayStr) >= 29:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
         
   elif monthStr == '3': #mar
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')

   elif monthStr == '4':#apr
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
      
   elif monthStr == '5': #may
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
         
   elif monthStr == '6': #jun
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
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
      else:
         print(date, 'is vaild')
         
   elif monthStr == '9': #sep
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
      
   elif monthStr == '10': #oct
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
         
   elif monthStr == '11': #nov
      if int(dayStr) >= 31:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
      
   elif monthStr == '12': #dec
      if int(dayStr) >= 32:
         print(date, 'is not vaild')
      else:
         print(date, 'is vaild')
   else:
      print('done')
main()
