# futval.py
# by Susan C. Feb 13 2015
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    #print("of a 10-year investment.")
    periods = eval(input("number of times that the interest is compounded each year "))
    principal = eval(input("How much will you invest: "))
    apr = eval(input("Enter the yearly interest rate: "))
    for i in range (10 * periods) :
       principal = principal * (1 + apr)
    print("The value in", periods,"years is: ", principal)

main()
