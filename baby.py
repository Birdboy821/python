#baby.py
#christopher amell 1/4/19
#calculates the total babysitting bill

def main():
   start = eval(input('what time did you start at(12:01 am is 0.01 and 11:30 pm is 23.30): '))
   leave = eval(input('what time did you leave at(12:01 am is 0.01 and 11:30 pm is 23.30): '))

   if leave >= 21.00:
      after = round((leave - 21.00), 2)

      time = leave - start
      befor = time - after
      
      price = (after*1.75)+(befor*2.50)
      print(time, after, befor, str(round(price, 2))+'$')
main()
   
