#Return the number of even integers in the list.


def count_even(nums):
    count=0
    # Write your code here
    for num in  nums:
        if num%2==0:
            count+=1
    return count
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 6]
    result = count_even(nums)
    print(result)
