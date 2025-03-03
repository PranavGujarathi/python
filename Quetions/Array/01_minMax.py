def find_max_min(arr):
    # Initialize max and min to the first element of the array
    max_element = arr[0]
    min_element = arr[0]
    
    # Iterate through the array to find max and min
    for num in arr:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num
    
    return max_element, min_element

# Sample Input
arr = [5, 3, 9, 2, 8]

# Function call and output
max_val, min_val = find_max_min(arr)
print(f"Maximum: {max_val}, Minimum: {min_val}")
