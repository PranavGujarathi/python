arr=[0,1,3]
n=len(arr)
total = n*(n+1)/2

sum=0
for i in arr:
    sum+=i

ans=total-sum
print(ans)

