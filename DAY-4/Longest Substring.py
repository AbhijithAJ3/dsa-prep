#return the length of the longest substring that contains no repeated characters.
def longest_substring(s):
    # Write your code here
    a=[]
    max_length=0
    for letter in s:
        while letter in a:
            a.pop(0)
        a.append(letter)
        max_length=max(max_length,len(a))
    return max_length


if __name__ == "__main__":
    s = "abcabcbb"
    result = longest_substring(s)
    print(result)