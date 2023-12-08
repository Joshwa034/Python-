
s="gHjjjcjn"
res=[]
op=""
for i in range(len(s)):
        if(s[i].islower()):
            num=(ord(s[i])-ord('a'))
            newch = (ord("A")+num)
            n=chr(newch)
            res.append(n)
        else:
            num=(ord(s[i])-ord('A'))
            newch = (ord("a")+num)
            n=chr(newch)
            res.append(n)
op= op.join(res)       
print(op)