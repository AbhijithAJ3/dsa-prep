#Given a string s, return the first character that appears exactly once in the string. If every character repeats, return None.


def first_unique_char(s):
    # Write your code here
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
     
    for key,value in freq.items():
        if value==1:
            return key
             
        

if __name__ == '__main__':
    s = "swwiissa"
    result = first_unique_char(s)
    print(result)
