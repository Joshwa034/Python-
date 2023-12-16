a = [2,4]
b = [16,32, 96]
ls=[]

# for i in range(a[1], b[0]+1):
#     if i%a[1]==0:
#         ls.append(i)
c=0

for i in range(max(a), min(b)+1, max(a)):
    ch=True

    for j in range(len(a)):
        if i%a[j]!=0:
            ch = False
            break
    for k in range(len(b)):
        if b[k]%i!=0:
            ch = False
            break
    if ch:
        c+=1
print(c)