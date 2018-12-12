# circle.py
# by christopher amell
# a program that is for circles

#def main():
   #r = eval(input("what is your radius "))
   #v = 4 / 3 * 3.14 * r ** 3
  # a = 4 * 3.14 * r ** 2
 #  print("the volume of your sphere is ",v ,"and you surface area is ",a,)
#main()

#def main():
 #  d = eval(input("what is your diameter "))
  # p = eval(input("what is your price "))
   #r = d / 2
   #a = 3.14 * r ** 2
  # cpsi = a * p
 #  print("the cost per square inch is",cpsi,)
#main()

#def main():
 #  h = eval(input("how many hydrogen do you have "))
  # c = eval(input("how many carbon do you have "))
   #o = eval(input("how many oxygen do you have "))

   #mw = h * 1.00794 + c * 12.0107 + o * 15.9994

   #print("your molecular weight is",mw,)
#main()

#def main():
 #  sec = eval(input("how long did the sound take to be heard for the flash "))
  # ft = 1100 * sec
   #mile = ft / 5280
   #print("the lightning strike was",mile,"miles away")
#main()

#def main():
   #pounds = eval(input("how many pounds do you have "))
  # cost = 10.50 * pounds + 0.86 * pounds +1.50
 #  print("the cost was $",cost,)
#main()

#def main():
  # x1, y1 = eval(input("what is your first point(in this form x1, y1) "))
   #x2, y2 = eval(input("what is your second point(in this form x2, y2) "))
  # slope = (y2 - y1) / (x2 - x1)
 #  print("the slop is",slope,)
#main()

def main():
   x1, y1 = eval(input("what is your first point(in this form x1, y1) "))
   x2, y2 = eval(input("what is your second point(in this form x2, y2) "))
   z = ( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2
   import math
   dis = math.sqrt(z)
   print("the distance is",dis,)
main()

#def main():
 #  year = eval(input("Waht year is it"))
  # C=year//100
   #epact=(8+(C//4)-C+((8*C+13)//25)+11*(year%19))%30
   #print("the epact of",year,"is",epact,)
#main()
   
#def main():
 #  a, b, c = eval(input("what are your side length(in this way s1, s2 ,s3) "))
  # import math
   #s = (a+b+c)/2
  # area = math.sqrt(s*(s-a)*(s-b)*(s-c))
 #  print("your area is",area,)
#main()

#def main():
 #  height = eval(input("what are your height of the ladder "))
  # angle = eval(input("what are your angle of the ladder in degrees "))
   #import math
   #radians = (math.pi/180)*angle
  # length = height/math.sin(radians)
 #  print(length)
#main()

#def main():
   #li = eval(input("how many numbers are being summed "))
   #x=0
   #for i in range(li):
   #   n = eval(input("what is your number "))
  #    x=x+n
 #  print(x)
#main()

#def main():
 #  li = eval(input("how many numbers are being summed "))
  # x=0
   #for i in range(li):
    #  n = eval(input("what is your number "))
     # x=x+n
   #print(x/li)
#main()

#def main():
   #n = eval(input("which place do you want "))
  # x=0
  # y=1
   #for i in range(n):
    #  z=y+x
   #   x=y
  #    y=z
 #  print(x)
#main()

#def main():
 #  n = eval(input("what number do you want to find to square root of "))
  # g = eval(input("What is your guess "))
   #p=(g+(n/g))/2
 #  print(p)
#main()



#def main():
 #  n = eval(input("which place do you want "))
  # summ = 0
   #while(n>0):
    #  summ=summ+n
     # n=n-1
   #print(summ)
#main()

#def main():
   #n = eval(input("which place do you want "))
   #summ = 0
   #while(n>0):
   #   summ=summ+n**3
  #    n=n-1
 #  print(summ)
#main()
