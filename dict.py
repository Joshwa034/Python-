# Enter your code here. Read input from STDIN. Print output to STDOUT

a ={}
c=0
for i in range(int(input())):
    w = input()
    if w in a:
        a[w]+=1
    else:
        a[w]=1
print(len(a))
print(*a.values())
    