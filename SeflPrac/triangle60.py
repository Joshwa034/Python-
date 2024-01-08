def tri(n):
    for i in range(1, n+1):
        space = n-i
        print(" "*space, end ="")

        for j in range(1, i+1):
            print("*", end =" ")
        print()
tri(4)

#    * 
#   * * 
#  * * * 
# * * * * 