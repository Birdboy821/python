#fibonacci.py
#christopher amell 1/3/19
#compute the nth Fibonacci number

def math(n):
   x=0
   y=1
   for i in range(n):
      z=y+x
      x=y
      y=z
   print(x)
def main():
   n = eval(input("which place do you want "))
   math(n)
main()
