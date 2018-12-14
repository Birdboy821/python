#name.py
#christopher amell 12-14-18
#The value of a name

def main():
   print('does not work with capital')
   word = input('what is your name ')
   
   x = 0
   z = 0
   for ch in list(word):
      y = (ord(word[x])-96)
      x += 1
      z = y + z
   print(z)
main()
