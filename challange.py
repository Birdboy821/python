#challange.py
#by christopher amell 11-19-2018 
#this is were all the challenges for 1.3 

#def main():
 #  x = eval(input("what is your X value "))
  # y = eval(input("what is your Y value "))
   #import math
  # z = math.pow(x,y)
 #  print(z)
#main()

#def main():
 #  customer = eval(input("How many customer do you have "))
  # time = customer * 4
   #print("It would take",time,"minutes to go through",customer,"customers")
#main()

#def main():
 #  bikesSales = eval(input("How many bikes did you sell "))
  # x = bikesSales // 5
   #revenue = 50 * x + 250 * bikesSales
  # print(revenue)
 #  print(x)
#main()

#def main():
 #  x = 1
  # for i in range(64):
   #   x = x * 2
   #print(x)
#main()

def main():
   have = eval(input("how much money do you need to give"))
   quart = have // 0.25
   res1 = have % 0.25
   dimes = res1 // 0.10
   res2 = res1 % 0.10
   nick = res2 // 0.05
   res3 = res2 % 0.05
   penn = res3 //0.01
   print("you nedd to give")
   print("Quarters",int(quart),)
   print("Dimes",int(dimes),)
   print("Nickels",int(nick),)
   print("Pennies",int(penn),)
main()
