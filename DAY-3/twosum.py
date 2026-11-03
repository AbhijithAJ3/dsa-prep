nums = [2, 7, 11, 15]
target = 9
seen={}

for index,num in enumerate(nums):
    needed=target-num
    if needed in seen:
        print(seen[needed],index)
        break
    else:
        seen[num]=index
    