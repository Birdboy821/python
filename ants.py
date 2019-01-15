#ants.py
#christopher amell 1/2/19
#print the lyrics for ten verses of "The Ants Go Marching."

def song(num, action):
   print('The ants go marching',num,'by',num+'.')
   print('Hoorah! Hoorah!')
   print('The ants go marching',num,'by',num+'.')
   print('Hoorah! Hoorah!')
   print('The ants go marching',num,'by',num+';')
   print('The little one stops to',action+',')
   print('And they all go marching down to the ground')
   print('To get out of the rain.')
   print('Boom, boom, boom, boom!')
   print()

def main():
   song('one','eat a pie')
   song('two','say bye')
   song('three','poke his eye')
   song('four','tie his shoe')
   song('five','look at the sky')
   song('six','cry')
   song('seven','talk to the fbi')
   song('eight','unify a revolution')
   song('nine','go up high')
   song('ten','die')
main()
