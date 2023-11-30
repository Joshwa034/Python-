
def plusMinus(arr):
    # Write your code here
    pc = 0
    mc = 0
    zc = 0
    n = len(arr)

    
    for i in range(0, len(arr)):
        if (arr[i]<0):
            mc+=1
        elif (arr[i]==0):
            zc+=1
        elif (arr[i]>0):
            pc+=1
    print(pc/n)
    print(mc/n)
    
    print(zc/n)
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
# 5
# 0 0 -1 1 1




def diagonalDifference(arr):
    # Write your code here
    fdig= 0
    sdig = 0
    n = len(arr)
    res = 0   # 2
    for i in range(0, len(arr)):
        
        n = n-1
        fdig += arr[i][i]
        sdig += arr[i][n]
        res = abs(fdig-sdig)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

def staircase(n):
    # Write your code here
    
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)
        
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

# 6



def miniMaxSum(arr):
    # Write your code here
    a = sorted(arr)
    a.pop()
    sum1 = sum(a)
    b = sorted(arr)
    b.pop(0)
    sum2 = sum(b)
    print(f"{sum1} {sum2}")
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# 1 2 3 4 5

def birthdayCakeCandles(candles):
    # Write your code here
    count = 0
    a = max(candles)
    for i in range(0, len(candles)):
        if candles[i] == a:
            count+=1
        
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
# 4
# 3 2 1 3