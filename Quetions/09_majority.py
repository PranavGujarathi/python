def find_majority_element(arr):
    arr.sort() 
    return arr[len(arr) // 2]  


arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Majority Element:", find_majority_element(arr))
