

A = set(map(int, input().split()))
flag = True

nB = int(input())

for _ in range(nB):
    B = set(map(int, input().split()))
    
    x = B-A
    if len(x) == 0:
        continue
    else:
        flag = False
        break

print(flag)
# a="1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78"
# A = set(map(int, a.split()))

# b="1 2 3 4 5"
# B = set(map(int, b.split()))

# x = B-A
# print(len(x))









