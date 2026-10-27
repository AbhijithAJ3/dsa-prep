'''Given a list of integers, move all zeroes to the end while maintaining the relative order of the non-zero elements.'''
def move_zeroes(nums):
    # Your solution
    pos=0
    for num in range(len(nums)):
        if nums[num]!=0:
            nums[num],nums[pos]=nums[pos],nums[num]
            pos+=1
    return nums
nums = [1,2,0,18,0,12]
print(move_zeroes(nums))