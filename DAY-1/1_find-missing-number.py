'''
You are given a list nums containing n distinct integers from the range 0 to n, inclusive. Exactly one number is missing.

Your task is to find and return the missing number.
'''

def missing_number(nums):
    # Write your solution here
    for i in range(len(nums)+1):
        if i not in nums:
            return i
        

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missing_number(nums))