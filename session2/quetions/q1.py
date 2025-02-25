
#  if both positive and negative are same 
def rearrange_array(nums):
    positive = []
    negative = []
    
    # Separate positive and negative numbers
    for num in nums:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)

    # Merge alternately
    ans = []
    for i in range(len(positive)):
        ans.append(negative[i])
        ans.append(positive[i])
    
    return ans

# Example usage
nums = [-1, 2, -3, 4, 5, -6]
result = rearrange_array(nums)
print(result)



#  if amout of positive and negative numbers are diffrent

lst = [-1, 2, -3, 4, 5, -6]

neg = []
pos = [] 
result = []
i=0
j=0

for ls in lst:
    if ls < 0:
        neg.append(ls) 
    else:
        pos.append(ls)

while i < len(neg) and j < len(pos):
    result.append(neg[i])
    result.append(pos[j])
    i += 1
    j += 1

print("Positives:", pos)
print("Negatives:", neg)

print(result)