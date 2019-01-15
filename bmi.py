#bmi.py
#christopher amell 1/4/19
#body mass index (BMI) is calculate

def main():
   weight = eval(input('what is your weight: '))
   height = eval(input('what is your height: '))

   bmi = weight * 720 / height ** 2

   if 19 <= bmi <= 25:
      print('you are considered healthy')
   elif bmi <19:
      print('your BMI is to low')
   else:
      print('Your BMI is to high')
   print(bmi)
main()
