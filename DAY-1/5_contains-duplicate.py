#Given a list of integers, return True if any value appears at least twice; otherwise, return False.
def contains_duplicate(nums):
    # Write your code here
    seen=set()
     
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
         

if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    result = contains_duplicate(nums)
    print(result)
