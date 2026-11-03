def second(nums):
     unique=sorted(set(nums))
     return unique[-2]

nums = [10, 5, 20, 8, 20]
print(second(nums))

