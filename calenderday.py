from calendar import weekday, day_name
a = list(map(int, input().split()))

na = weekday(a[2], a[0], a[1])
res = day_name[na].upper()
print(res)