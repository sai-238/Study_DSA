string = "abc3b4c5"
l , r = 0, 0
res = ""
for c in range(len(string)):
    if string[c].isalpha():
        r += 1
    else:
        res +=  int(string[c]) * string[l:r]
        r +=1
        l = r
print(res)