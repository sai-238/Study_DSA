st = "abc7de5"
number = ""
text = ""
res = []
for i in st :
    if (i.isnumeric()):
        number += i    
    else:
        text += i
res.append(text)      
res.append(number)
print(" The text and numbers are splited : " +str(res))

