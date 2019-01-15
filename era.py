#era.py
#christopher amell 1/4/19
#a program the calculates a pitcher’s earned run average

def ERA(runs, pitched):
   era = 9 * runs / pitched
   print(round(era, 2))

def main():
   runs = eval(input('what is the total number of earned runs allowed '))
   pitched = eval(input('what is the total number of innings pitched '))
   ERA(runs, pitched)
main()
