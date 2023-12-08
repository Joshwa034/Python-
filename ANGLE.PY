# Enter your code here. Read input from STDIN. Print output to STDOUT\

import math

a = int(input())

b = int(input())

div = a / b

res1 = round(math.degrees(math.atan(div)))

print(f"{res1}\u00b0")