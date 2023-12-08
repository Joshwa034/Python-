a=[]
b=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    a.append(name)
    a.append(score)
    
alps=(a[1::2])
alps.sort()
po=alps.pop(0)
for i in range(len(alps)):
    if(po == alps[0]):
        alps.pop(0)
res=[]
for i in range(len(a)):
    if(alps[0]==a[i]):
        res.append((a[i-1]))
res.sort()
for i in range(len(res)):
    print(res[i])
