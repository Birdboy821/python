#acronym2.py
#christopher amell 1/3/19
#a program that allows the user to type in
#a phrase and then outputs the acronym for that phrase

def acronym(phrase):
   q = phrase.split(" ")

   x = 0
   y = ''
   for ch in q:
      word = q[x]
      y += word[0].upper()
      x += 1
   print(y)
def main():
   phrase = input('what is your saying: ')
   acronym(phrase)
main()
