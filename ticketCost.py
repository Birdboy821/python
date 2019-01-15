#tickitCost.py
#christopher amell 1/4/19
#The speeding ticket fine policy in Lazytown 

def main():
   limit = eval(input('what is the speed limit: '))
   clocked = eval(input('what is your clocked speed: '))

   if clocked > 90:
      over = clocked - limit
      cost = 50 + over * 5 + 200
      print(str(cost) + '$')

   elif clocked > limit:
      over = clocked - limit
      cost = 50 + over * 5
      print(str(cost) + '$')

main()
