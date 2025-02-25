a= input("Enter character : ")

if (a.isupper()):
    print("Character is upercase")
elif(a.islower()):
    print("character is lowercase")
elif(a.isdigit()):
    print("character is digit ")
else:
    print("character is special character")

    # without using inbuild functions 

#  with ascii code 

b=ord(input("Cnter the character : "))

if b >= 65 and b <= 90:
    print("Upper case")
elif b >= 97 and b <= 122:
    print("Lower case")
elif b >= 48 and b <= 57:
    print("Its a digit")
else:
    print("Other Special symbol")


