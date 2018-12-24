#sentWordAvg.py
#christopher amell 12/24/2018
#Write a program that calculates
#the average word length in a sentence entered by the user

def main():
    sent = input('what is your sentence ')
    x = 0
    r = 0
    for i in sent.split(' '):
          y = sent.split(' ')[x]
          c = 0
          d = 0
          for v in list(y):
              d += 1
              t = d
          x += 1
          #print(x , y , d)
          r += t
    print(r/x)
main()
