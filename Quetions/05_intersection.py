arr1=[1,2,2,1]
arr2=[2,2]

common=[]

for i in arr1:
    if i in arr2:
        common.append(i)


print(common)

