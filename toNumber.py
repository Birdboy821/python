#toNumber.py
#christopher amell 1/3/19
#list of strings, each of which represents a number

def toNumbers(strList):
   x = 1
   listt = []
   for char in strList:
      print(x)
      listt.append(str(x))
      print(listt)
      x+=1
       
def main():
    sttr = ['one','two', 'three','four']
    toNumbers(sttr)
main()
