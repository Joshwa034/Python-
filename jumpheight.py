
def hurdleRace(k, height):
    # Write your code here
    
    maxh = max(height)
    
    if maxh==k or maxh <k:
        return 0
    else:
        rs = maxh - k
        return rs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)