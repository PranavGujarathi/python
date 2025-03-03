def product_except_self(arr):
    n = len(arr)
    result = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i == j: 
                continue
            product *= arr[j]
        result.append(product)

    return result

# Example usage:
arr = [1, 2, 3, 4]
print("Product Except Self:", product_except_self(arr))
 