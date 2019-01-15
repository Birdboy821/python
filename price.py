#price.py
#christopher amell
# calculates the price on an
#item on sale, given the regular price and the sales percentage

def math(price, sale):
   newPrice = price * (sale/100)
   print(price - newPrice)


def main():
   price = eval(input('what is the actual price '))
   sale = eval(input('what is the sale percentage(dont include %) '))
   math(price, sale)
main()
