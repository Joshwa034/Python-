n = 6

for i in range(n):
    spaces = i
    print(" "*spaces, end="")
    for j in range(n-i):
        print('*', end =" ")
    print()
