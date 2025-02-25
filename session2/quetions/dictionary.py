'''
arr={}
arr[1]=1
arr['1']=2
arr[1] +=1
sum=0
for k in arr:
    sum += arr[k]
print(sum)
'''
'''
my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4
sum=0

for i in my_dict:
    sum+=my_dict[i]

print(sum)

'''

my_dict={}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12

sum=0
for i in my_dict:
    sum+=my_dict[i]

print(sum)
print(my_dict)
