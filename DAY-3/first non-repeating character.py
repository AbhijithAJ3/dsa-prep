s = "aabbcde"
freq={}
for letter in s:
    if letter in freq:
        freq[letter]+=1
    else:
        freq[letter]=1
for key,value in freq.items():
    if value==1:
        print( key)
        break