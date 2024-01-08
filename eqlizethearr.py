#!/bin/python3

import math
import os
import random
import re
import sys

def equalizeArray(arr):
    # mx = max(arr)
    # count = arr.count(mx)
    setarr = set(arr)
    mx = 0
    
    for i in setarr:
        if arr.count(i) > mx:
            mx = arr.count(i)
        
    res = len(arr) - mx
    return res
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
