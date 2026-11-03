#Given an integer list nums, return a list where each element is the product of every number in nums except the number at that index.
nums=[1, 2, 3, 4]
right=[]
left=[]
final=[]
for i in range(len(nums)):
    result=1
    for j in range(i+1,len(nums)):
        
        result=nums[j]*result
    right.append(result)
print(right)
for i in range(len(nums)):
    result=1
    for j in range(0,i):
        result*=nums[j]
    left.append(result)
print(left)

for i in range(len(nums)):
    final.append(left[i]*right[i])
print(final)