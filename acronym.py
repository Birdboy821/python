#acronym.py
#christopher amell 12-14-18
#a program that allows the user to type in
#a phrase and then outputs the acronym for that phrase

def main():
   word = input('what is your saying ').split(" ")

   x = 0
   for ch in word:
      print(word[x][0].upper())
      x += 1
main()
