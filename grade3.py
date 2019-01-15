#grade3.py
#christopher amell 1/3/19
#a letter grade calculater for a 5 question quiz

def grade(score):
   letter = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAAA"
   print(letter[score])

def main():
   score = eval(input('what is the number right: '))
   grade(score)
main()
