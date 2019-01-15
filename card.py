#card.py
#christopher amell 1/15/2019
#a program that prompts for a credit card and emits the name of the brand

def main():
   card = input("what is your credit card number: ")

   first = card[0]

   if first == '4':
      print('Visa')
   elif first == '5':
      print('MasterCard')
   elif first == '6':
      print('Discover')
   else:
      print('Unknown Card')
main()
