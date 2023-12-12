n, m = input().split()
N = int(n)
M = int(m)

dot = ".|."
   
for i in range(1,int((N+1)/2)):   
    print((dot*(i+(i-1))).center(M,"-"))

print("WELCOME".center(M, '-'))

for i in range(int(N//2),0,-1):
    print((dot*(i+(i-1))).center(M,"-"))