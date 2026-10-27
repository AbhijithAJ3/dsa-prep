'''Given a list of integers nums and an integer target, return the indices of the two numbers that add up to the target.

Assume exactly one valid pair exists, and you cannot use the same element twice.'''
def two_sum(nums, target):
    # Your solution here
    seen={}
    for index,num in enumerate(nums):
        needed=target-num
        if needed in seen:
            return seen[needed],index
        else:
            seen[num]=index
        

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))