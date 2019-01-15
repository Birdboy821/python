#classifies.py
#christopher amell 1/4/19
# program that calculates class standing from the number of credits earned

def main():
   credit = eval(input('how many credits do you have: '))
   if credit < 7:
      print('Freshman')
   elif 16 > credit >= 7:
      print('sophomore')
   elif 26 > credit >= 16:
      print('junior')
   else:
      print('senior')
main()
