#grade4IThink.py
#christopher amell 1/4/19
#a program that accepts a quiz score for a 5 question quiz

def main():

   grade = eval(input('what is your grade: '))

   if 90 <= grade <= 100:
      print('you got an A')
   elif 80 <= grade <= 89:
      print('you got a B')
   elif 70 <= grade <= 79:
      print('you got a C')
   elif 60 <= grade <= 69:
      print('you got a D')
   elif grade <= 59:
      print('you got a F for FAILURE')
   else:
      print('you either put a number bigger or smaller then 100-0')

main()
