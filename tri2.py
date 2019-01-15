#tri2.py
#christopher amell 1/3/19
# computes the area of a triangle given the length of its three sides 

from math import *
def mathTri(a, b, c):
   s = (a+b+c)/2
   area = sqrt(s*(s-a)*(s-b)*(s-c))
   print("your area is",area,)

def main():
   a, b, c = eval(input("what are your side length(in this way s1, s2 ,s3) "))
   mathTri(a, b, c)
main()
