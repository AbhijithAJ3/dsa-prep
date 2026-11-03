intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged=[]
for i in intervals:
    if not merged or merged[-1][1]<i[0]:
            merged.append(i)
    else:
          merged[-1][1]=max(merged[-1][1],i[1])
print(merged)