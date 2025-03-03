inputString=str(input("Enter string : "))
count=0

for i in inputString:
    if i.isalnum() == False and not i.isspace():
        count+=1


print(f"Total Special Characters present = ", count)

