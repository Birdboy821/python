#sphere.py
#christopher amell 1/3/19
#a program that calculate a spheres area and volume

def sphereArea(radius):
   a = 4 * 3.14 * radius ** 2
   print(a)
   
def sphereVolume(radius):
   v = 4 / 3 * 3.14 * radius ** 3
   print(v)

def main():
   r = eval(input('what is your radius: '))
   sphereArea(r)
   sphereVolume(r)
   
main()
