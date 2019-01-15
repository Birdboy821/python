#oldMacDonald.py
#christopher amell 1/2/19
#print the lyrics for five different animals

def song(animal, sound):
   
   #animal = ['cow' , 'moo' , 'chicken' , 'cluck' , 'dog' , 'bark' , 'cat' , 'meow' , 'pig' , "I'm Bacon"]

   print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
   print("And on that farm he had a ",animal,", Ee-igh, Ee-igh, Oh!")
   print("With a ",sound,",",sound," here and a ",sound,"," ,sound, "there.")
   print("Here a ",sound,", there a" ,sound,", everywhere a" ,sound,"," ,sound+".")
   print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
   print()

def main():
   song('cow', 'moo')
   song('chicken', 'cluck')
   song('dog', 'bark')
   song('cat', 'meow')
   song('pig', "I'm Bacon")
main()
