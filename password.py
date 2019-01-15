#password.py
#christopher amell 1/15/2019
#taking in input and spiting out if the bill was pass


def main():
   password = input('What is your password: ')
   x = 0

   for i in list(password):
      x += 1
   if x >= 12:
      print("Storng password")
   elif 12 > x > 8:
      print("Moderately password")
   elif x < 8:
      print("Weak password")
   else:
      print("ERROR")
main()
