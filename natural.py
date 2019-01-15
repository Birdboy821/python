#natural.py
#christopher amell 1/3/19
#find the sum and sum of the cubed of the natural
#numbers up to one that is imputed by the user

def sumN(n):
   summ = 0
   while(n>0):
      summ=summ+n
      n=n-1
   print(summ)

def sumNCubes(n):
   summ = 0
   while(n>0):
      summ=summ+n**3
      n=n-1
   print(summ)

def main():
   n = eval(input("which place do you want: "))
   sumN(n)
   sumNCubes(n)
main()
