from collections import Counter

def highest_repeated_count(arr):
    # Use Counter to count occurrences of each element in the array
    counts = Counter(arr)
    
    # Find the maximum count
    max_count = max(counts.values())
    
    # Count how many numbers have the maximum count
    num_of_highest_repeated_numbers = sum(1 for count in counts.values() if count == max_count)
    
    return num_of_highest_repeated_numbers

# Example usage:
my_array = [1, 2, 2, 2, 3, 3, 3, 4]
result = highest_repeated_count(my_array)

print(result)
