'''
You are given two strings, s and t.

Return True if t is an anagram of s; otherwise, return False.
'''
def is_anagram(s, t):
    # Your solution here
    if(sorted(s)==sorted(t)):
        return True
    else:
        return False
s = "listen"
t = "silent"
print(is_anagram(s,t))