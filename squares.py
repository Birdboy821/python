#squares.py
#christopher amell 1/3/19
#a program that computes the sum of the squares of numbers read from a file

def math(file):
   numInFile = open(file , 'r')
   numOutFile = open(file , 'a')

   list1 = numInFile.readlines()

   x = 0
   for i in list(list1):
      print(int(list1[x]) ** 2)
      x +=1

def main():
   file = input('what file has your number: ')
   math(file)
main()
