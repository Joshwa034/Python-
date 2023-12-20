
def extraLongFactorials(n):
    # Write your code here
    res = 1
    i=0
    while True:
        res= res * (n-i)
        # print(f"{res} = {res} *{n-i}")
        i+=1
        # print(n-i)
        # print(f"{res}\n")
        if (n-i) == 0:
            break
    print (res)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
