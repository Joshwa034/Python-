#!/bin/python3

import math
import os
import random
import re
import sys

# def appendAndDelete(s, t, k):
#     if (s == t):
#         return ('Yes')
#     else:
#         sl= list(s)
#         # print(sl)
#         st = list(t)
#         # print(st)
#         c=0
#         for i in range(len(s)):
#             if (i== len(st)):
#                 break
#             elif (sl[i] == st[i]):
#                 c+=1
#                 print(i, c, sl[i], st[i])
#             else:
#                 break
#         s1l = len(sl) - c
#         s2l = len(st) - c
#         summ = s1l+s2l
#         if summ <= k:
#             return ('Yes')
#         else:
#             return ('No')

def appendAndDelete(s, t, k):
    d = abs(len(s)-len(t))
    for i in range(min(len(s), len(t))):
        if s[i]!=t[i]:
            delete = len(s) - i
            break
        delete = 0

    if len(s)<=len(t):
        append = delete + d
        
    if len(t)<=len(s):
        append = len(t)-(len(s)-delete)
    
    mink = delete + append
    if (k>=mink and (k%2==0 if mink%2==0 else k%2==1)) or k>len(s)+len(t):
        return 'Yes'
    return 'No'

                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
