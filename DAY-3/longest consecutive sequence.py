nums = [100, 4, 200, 1, 3, 2,101,102,103,104,105,106]
nums=sorted(nums)
max_length=1
current_length=1
for i in range(1,len(nums)):
    if nums[i]==nums[i-1]+1:
        current_length+=1
    else:
         
        current_length=1
    max_length=max(max_length,current_length)

print(max_length)