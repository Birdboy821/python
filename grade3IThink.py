#grade3IThink.py
#christopher amell 1/4/19
#a program that accepts a quiz score for a 5 question quiz

def main():

   grade = eval(input('what is your grade: '))

   if grade == 5:
      print('you got an A')
   elif grade == 4:
      print('you got a B')
   elif grade == 3:
      print('you got a C')
   elif grade == 2:
      print('you got a D')
   elif grade == 1:
      print('you got a F')
   elif grade == 0:
      print('you got a F for FAILURE')
   else:
      print('you either put a number bigger or smaller then 5-0')

main()
