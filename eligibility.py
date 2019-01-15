#eligibility.py
#christopher amell 1/4/19
#eligibility for the Senate and House

def main():
   age = eval(input('What is your age: '))
   citizen = eval(input('How long have you been a citizen: '))

   if age >= 30 and citizen >= 9:
      sen = 1
   else:
      sen = 2

   if age >= 25 and citizen >= 7:
      rep = 1
   else:
      rep = 2

   if sen == 1:
      print('You are eligibility for the Senate and House')
   elif sen == 2 and rep == 1:
      print('You are eligibility for the House, but not the Senate')
   else:
      print('You are not eligibility for either House or Senate') 
main()   
