#sumList.py
#christopher amell 1/3/19
#sums of a list

def sumList(nums):
   t = 0
   for i in list(nums):
      t += int(i)
      print(t)

def main():
   nums = input('what is your list: ').split(' ')
   sumList(nums)
main()
