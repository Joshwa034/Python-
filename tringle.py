# Set the value of i (you can change this to any desired number)
i = 5

# Create a list of numbers from 1 to i
numbers_list = []
for j in range(1, i + 1):
    numbers_list.append(str(j))

# Concatenate the numbers into a single string
result_string = "".join(numbers_list)

# Print the result string followed by a space
print(result_string, end=" ")
