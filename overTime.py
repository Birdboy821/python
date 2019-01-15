#overTime.py
#christopher amell 1/4/19
#calculate the total wages for the week

def main():
   time = eval(input('how many hours did you work: '))
   rate = eval(input('what is your hourly rate: '))

   if time <= 40:
      pay = time * rate
      print(pay)
   elif time > 40:
      half = time - 40
      pay = ((time - half) * rate) + (half * (rate + (half / 2)))
      print(pay)
   else:
      print('you may have any error')
main()
   
