
'''
a = [1,2,3,4,5,6,7,8,9]
a[::2] = 10,20,30,40
'''

'''
def func(value,values):
    var = 1
    values[0] = 44
    
t = 3
v = [1,2,3]

func(t,v)
print(t,v[0])

output - 3 44
'''


data = [
    [ [1, 2], [3, 4] ],  # data[0] (first 2D list)
    [ [5, 6], [7, 8] ]   # data[1] (second 2D list)
]

'''
def fun(m):
    v = m[0][0]  # Initialize v with the first element of the first row
    for row in m:   # Loop through each row
        for ele in row:   # Loop through each element in the row
            if v < ele:  
                v = ele   # Update v if ele is greater
    return v   # Return the maximum value


print(fun(data[0]))
'''
'''
arr=[[1,2,3,4],
     [4,5,6,7],
     [8,9,10,11],
     [12,13,14,15]]
for i in range(0,4):
    print(arr[i].pop() , end=" ")

    
    o/p : 4 7 11 15 
'''
'''
def fun(i,values=[]):
    values.append(i)
    # print(values)
    return values

fun(1)
fun(2)
fun(3)
'''

'''
arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i], end=" ")
    
'''

fl1=["Apple","Berry", " Cherry","Papaya"]
fl2=fl1   # list alising 
fl3=fl1[:]
fl2[0]="Guava"
fl3[1]="kiwi"

sum = 0
for ls in (fl1,fl2,fl3):
    if ls[0] == "Guava":
        sum+=1
    if ls[1]=="kiwi":
        sum+=20
print(sum)



