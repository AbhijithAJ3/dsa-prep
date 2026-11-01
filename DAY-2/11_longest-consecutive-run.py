#Given a string, return the length of the longest run of the same character appearing consecutively.


def longest_run(s):
    # Write your code here
    current_run=1
    max_run=1
    for i in range(1,len(s)):
       if s[i]==s[i-1]:
           current_run+=1
       else:
           current_run=1 
       if max_run<current_run:
             max_run=current_run
    return max_run
if __name__ == '__main__':
    s = "aaabbccccd"
    result = longest_run(s)
    print(result)
