a=50
b=30
c=20
d=10

# some random maths shit
print((a+b)*c/d)        # 80*20/10 = 80*2
print((a+b)*(c/d))      # 80*2 
print(a+(b*c)/d)


#  list 

roll_no=[3,5,7,9,11,4,5,2]
for x in roll_no:
    if(x %2==0):
        print("even no found is : " , x)
        break

counter=[2,1,4,5,5,4,4,1,1]
count=0
even=0
odd =0

for i in counter:
    if i==4:
        count+=1
    elif i%2==0:
        even+=1
    elif i%2!=0:
        odd+=1

print(count-even)
print(count-odd)