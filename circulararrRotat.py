
import math
import os
import random
import re
import sys

def circularArrayRotation(a, k, queries):
    # Write your code here
    arr = a
    
    for i in range(k):
        arr0 = arr.pop()
        arr.insert(0, arr0)
    ls = []
    
    for j in (queries):
        a = (arr[j])
        ls.append(a)
    return ls
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)