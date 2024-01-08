n = 15
for i in range(1,n+1):
    for j in range(1, i +1):
        if(i <=2):
            print("*", end ='')
        elif(i>2):
            
            if( i <n):
                if j>1 and j <i:
                    print(" ", end ="")
                else:
                    print(f"*", end ='')
            else:
                print("*", end='')
    print()