def move_zeros(arr):
    non_zeros = [] 
    zero_count = 0 

    for num in arr:
        if num != 0:
            non_zeros.append(num)  
        else:
            zero_count += 1 

    while zero_count > 0:
        non_zeros.append(0)
        zero_count -= 1  

    return non_zeros

# Example usage:
arr = [0, 1,0 , 0, 3,0, 12]
print("After Moving Zeros:", move_zeros(arr))
