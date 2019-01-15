#pizza.py
#christopher amell 1/3/19
#compute the area of a pizza

def pizzaArea(d, p):
   r = d / 2
   a = 3.14 * r ** 2
   cpsi = a * p
   print("the cost per square inch is",cpsi,)

def main():
   d = eval(input("what is your diameter "))
   p = eval(input("what is your price "))
   pizzaArea(d, p)
main()
