# # Given a list of intervals where each interval is represented as [start, end], merge all overlapping intervals and return a list of the non-overlapping intervals in sorted order.

# # Two intervals overlap if the next interval’s start is less than or equal to the current interval’s end.

# Input:
# 4
# 1 3
# 2 6
# 8 10
# 15 18

# Output:
# [[1, 6], [8, 10], [15, 18]]

def merge_intervals(intervals):
    # Write your code here
    merged=[]
    for i in range(len(intervals)):
        for j in  range(i+1,len(intervals)):
            if intervals[i][0]>intervals[j][0]:
                intervals[i],intervals[j]=intervals[j],intervals[i]    
    
    for i in intervals:
        if not merged or merged[-1][1]<i[0]:
            merged.append(i)
        else:
            merged[-1][1]=max(merged[-1][1],i[1])
    return merged
if __name__ == "__main__":
    n = int(input())
    intervals = []

    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])

    result = merge_intervals(intervals)
    print(result)