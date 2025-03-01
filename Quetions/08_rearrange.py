def rearrange_alternate(arr):
    positive = []  
    negitive = []  

    
    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negitive.append(num)

    result = []  
    i, j = 0, 0

    
    while i < len(negitive) and j < len(positive):
        result.append(negitive[i])
        result.append(positive[j])
        i += 1
        j += 1


    result.extend(positive[j:])
    result.extend(negitive[i:])

    return result

# Example usage:
arr = [-1, 2, -3, 4, 5, -6]
print("Rearranged Array:", rearrange_alternate(arr))
