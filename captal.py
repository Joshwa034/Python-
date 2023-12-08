def solve(s):
    res=''
    res=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==" ":
            k=s[i].upper()
            res+=k
        else:
            res+=s[i]
    return res

j=solve("ssjj")
# print(j[0].upper())
print(j)