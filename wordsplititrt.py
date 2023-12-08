from itertools import permutations

word, num = input().split()
result = sorted(''.join(values) for values in permutations(word, int(num)))
print("\n".join(result))
