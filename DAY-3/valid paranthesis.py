s = "({[]}[}])"
stack=[]
pair={
    ')':'(',
    ']':'[',
    '}':'{'
}
valid=True
for char in s:
    if char in '{([':
        stack.append(char)
    else:
        if not stack or stack[-1]!=pair[char]:
             valid=False
             break
        stack.pop()
print(valid and len(stack)==0)