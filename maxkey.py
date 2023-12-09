my_dict = {'a': 10, 'b': 5, 'c': 10, 'd': 15}

max_value = float('-inf')  # Start with negative infinity to ensure any value will be greater
key_with_max_value = None

for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        key_with_max_value = key

print(f"The key with the maximum value is: {key_with_max_value}")
