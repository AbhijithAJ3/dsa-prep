
def reverse_string(s):
    # Write your code here
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
    return rev


if __name__ == '__main__':
    s = "Python"
    result = reverse_string(s)
    print(result)
