arr=[3, 2, 3, 1, 2, 4,1,2,3,4,5,6]

unique=[]

# for i in arr:
#     if i not in unique:
#         unique.append(i)

# print(unique)


for i in range(0,len(arr)):
    if arr[i] not in unique:
        unique.append(arr[i])

print(unique)

