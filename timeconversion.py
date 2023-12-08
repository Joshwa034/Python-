#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    a = s[8:]
    b=""
    if s[:2] == "12":
        b="00"
        b = b+s[2:8]
    if (a == "PM"):
        b = s[:2]
        if (b== "12"):
            b = s[:8]
        else:
            
            c = int(b)
            c+=12
            b=str(c)+s[2:8]
    elif (a=="AM"):
        if (s[:2]=="12"):
            b="00"
            b = b+s[2:8]
        else:
            
            b = s[:8]
    
        
        
    
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
