from collections import Counter
n = int(input())

ls = list(input().split())
print(ls)

dic = Counter(ls)
print(dic)
total =0
for i in range(int(input())):
    s, p = input().split()
    if dic[s] != 0:
        total += int(p)
        dic[s]-=1
print(total)
