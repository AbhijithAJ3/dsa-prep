#Given a list of integers, return the largest number in the list.


def find_maximum(nums):
    # Write your code here
    max_num=nums[0]
    for num in nums:
        
        if num>max_num:
            max_num=num
    return max_num

if __name__ == '__main__':
    nums =  [3, 9, 2, 7]
    result = find_maximum(nums)
    print(result)
