left = ''
right = ''

for i in range(1, int(input())+1):
    left = left + str(i)
    
    if i != 1:
        right = str(i - 1) + right
        
    print(left + right)

#######################3

for i in range(1, int(input())+1):
    print(pow((((10**i - 10))//9) + 1, 2))