def majority_element(nums):
    nums.sort()  # Sort the list
    return nums[len(nums) // 2]  # Return the middle element

# Example usage
nums = [3, 2,2,2,3,3,2,2,2]
print(majority_element(nums))  # Output: 2
