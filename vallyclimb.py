
def countingValleys(steps, path):
    # Write your code here
    res = 0
    val = 0
    for i in range(len(path)):
        if path[i] =='D':
            res-=1
            
        elif (path[i]=='U'):
            res+=1
        
        if res == 0 and path[i]=='U':
            val+=1

    return val
    
    
# def countingValleys(steps, path):
#     # Write your code here
#     c1 = 0
#     c2 = 0
#     for i in path:
#         if i == 'D':
#             c1 -= 1
#         elif i == 'U':
#             c1 += 1
#         if c1 == 0 and i == 'U':
#             c2 += 1
#     return c2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)