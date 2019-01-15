#city.py
#christopher amell 1/4/19
#calculates the distance in miles between to cities
from math import *
def imp(first, second):
   dis = sqrt((first[0] - second[0])**2+(first[1]-second[1])**2)
   if dis < 1:
      ftdis = dis * 5280
      print('your 2 citys are less then a mile away')
      print(dis,'miles or', ftdis, 'feet away')
   else:
      print(dis)

def met(first, second):
   dis = sqrt((first[0] - second[0])**2+(first[1]-second[1])**2)
   if dis < 1:
      ftdis = dis * 1000
      print('your 2 citys are less then a kilometer away')
      print(dis,'kilometer or', ftdis, 'meters away')
   else:
      print(dis,'kilometers')
   

def main():
   first = eval(input("what is your first city's coordinates "))
   second = eval(input("what is your second city's coordinates "))
   con = eval(input("What unit do you want the distanst in(1 is USA, 2 is metric)"))

   if con == 1:
      imp(first, second)

   elif con == 2:
      met(first, second)
   else:
      print('ERROR')
main()
