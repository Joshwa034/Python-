seq = "123$456%789*0^"
output = "098$765%432*1^"

chars = ['$', '%', '*', '#', '^']
nums = []

for i in range(len(seq)):
    if seq[i] not in chars:
        nums.append(seq[i])

nums.reverse()

for j in seq:
    if j in chars:
        idx = seq.index(j)
        nums.insert(idx, j)

reverse = "".join(nums)

print(reverse)
