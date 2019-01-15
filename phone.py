#phone.py
#christopher amell 1/15/2019
#a program that prompts for a phone number, and determines whether
#or not it is a valid 10-digit number by ignoring any punctuation

def main():
   num = 0
   phone = input("What is you phone number: ")

   p = list(phone)

   if "-" in p:
      p.remove("-")
   else:
      p = p
   if "(" in p:
      p.remove("(")
   else:
      p = p
   if ")" in p:
      p.remove(")")
   else:
      p = p

   for i in list(p):
      num += 1
   if num == 10:
      print("vaild phone number")
   else:
      print("invail phone number")
main()
      
