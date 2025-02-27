def find_second_largest(arr):
    if len(arr) < 2:
        print("Array must have at least two elements")
        return -1

    largest = arr[0]
    second_largest = -1 

   
    for num in arr[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != -1 else -1


arr = [7, 3, 9, 2, 8]

# Function call and output
second_largest = find_second_largest(arr)

if second_largest != -1:
    print(f"Second Largest: {second_largest}")
else:
    print("No second largest element found")
