# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan C.

def main () :
    print("We give you what celsius and fahrenheit is.")
    celsius = -10
    for i in range(11):
        celsius = celsius + 10
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit and the temperature is", celsius, "degrees Celsius.")
main ()
