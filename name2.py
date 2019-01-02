#name2.py
#christopher amell 12-23-18
#The value of a name

def main():
    print('does not work with capital')
    print('make sure to have two space')
    word = input('what is your name ')
   
    x = 0
    z = 0
    for ch in list(word):
       y = (ord(word[x])-96)
       z = y + z
       x += 1
    print(z + 128)
main()

