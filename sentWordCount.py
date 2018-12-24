#sentWordCount.py
#christopher amell 12/24/2018
#program that counts the number of words in a sentence entered by the user

def main():
    sent = input('what is your sentence ')
    x = 0
    for i in sent.split(' '):
          x += 1

    print(x)
main()
