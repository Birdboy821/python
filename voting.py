#voting.py
#christopher amell 1/15/2019
#taking in input and spiting out if the bill was pass

def yn(house, yes):
   if house == 'representatives':
      v = 435/2
      if 435 > yes > v:
         print("True, the bill received enough votes to pass")
      elif 0 < yes < v:
         print('False, the bill did not pass')
      else:
         print("ERROR")

   elif house == 'senate':
      if 100 > yes > 50:
         print("True, the bill received enough votes to pass")
      elif 0 < yes < 50:
         print('False, the bill did not pass')
      else:
         print("ERROR")
   else:
      print("ERROR", yes, house)

def main():
   house = input("What house is voting(no captails): ")
   yes = eval(input("How many said yes: "))

   yn(house, yes)
main()
      
