def fib(fpage, spage, finalpage):
    a= fpage
    b=spage
    c = finalpage

    if (a>b) or (a<=0) or (b<=0):
        print("invalid input")
    else:
        arr=[0]*c
        arr[0]=a
        arr[1]=b
        for i in range(2, c):
            arr[i]=arr[i-1]+arr[i-2]
        print(arr[c-1])
fib(1,2,5)

s="796115110113721110141108"
s= s[::-1]
print(s)
res=""
i=0
while(i<len(s)-1):
    x = s[i]+s[i+1]
    if(x == "32"):
        res+=" "
    elif(int(x) in range(65,91) or int(x) in range(97,100)):
        res += chr(int(x))
    elif(i+2<len(s)):
        x = x+s[i+2]
        res += chr(int(x))
        i+=1
    i+=2
print(res)





