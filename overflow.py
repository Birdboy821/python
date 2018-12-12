# pi.py
# by christopher amell
# a program that is for approximates the value of pi
def main():
    n = int(input("how many terms do you want to summon"))
    total = 0
    for i in range(0,n,2):
        total += ((1.0/(i+i+1))-(1.0)/(i+i+3))

    pie = 4*total
    import math
    print(pie - math.pi)

main()
