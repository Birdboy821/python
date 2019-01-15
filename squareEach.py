#squareEach.py
#christopher amell 1/3/19
#squares a number in a list

def squareEach(nums):
   x = 0
   for i in list(nums):
      print(int(nums[x]) ** 2)
      x +=1

def main():
   nums = input('what is your list: ').split(' ')
   squareEach(nums)
main()
