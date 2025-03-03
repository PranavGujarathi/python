def rotate_array(arr, steps):
    steps = steps % len(arr)  
    return arr[-steps:] + arr[:-steps]  


arr = [1, 2, 3, 4, 5]
steps = 2
print(rotate_array(arr, steps))  # Output: [4, 5, 1, 2, 3]
