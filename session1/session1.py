#string manipulation 

s1="hello"
s2="world !"
result = s1 +" "+ s2
print(result)

s = "Python "
print(s * 3)  # Output: Python Python Python 


s="Python"
print(s[0])
print([-1])

s="Python"
print(s[1:4])
print(s[:3]) # from start to 2nd index
print(s[3:]) # from 3rd index to last
print(s[::-1])  #reverse

#len()
print(len(s))

#changing case 
s = "hello World"
print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world
print(s.title())  # Output: Hello World 
print(s.capitalize())  # Output: Hello world
print(s.swapcase())  # o/p : HELLO wORLD upper la lower karto , lower la upper karto 

#checking string 
s="hello123"
print(s.isalpha()) # false 
print(s.isdigit()) # False (Not only digits)
print(s.isalnum())  # True (Alphanumeric)
print(s.isspace())  # False (Not only spaces)


s = "Hello World"
print(s.find("World"))  # Output: 6 (Index return karto , string cha starting vala index) 
print(s.find("python"))  # return -1 if not present 

# replace karto word present asel tr 
# print(s.replace("World", "Python"))  # Output: Hello Python

#nasel tr tasach vapas karto 
print(s.replace("Word", "Python")) 



# tpyecasting 

# Implicit Type Casting (Automatic Conversion)
a = 5           # int
b = 2.5         # float
c = a + b       # int is automatically converted to float
print("Implicit Casting:", c, type(c))  # Output: 7.5 <class 'float'>

# Explicit Type Casting (Manual Conversion)
x = 10.75
y = int(x)  # Float to Integer (Truncates decimal part)
print("Float to Int:", y, type(y))  # Output: 10 <class 'int'>

s = "100"
num = int(s)  # String to Integer
print("String to Int:", num + 5, type(num))  # Output: 105 <class 'int'>

# List to Tuple and Vice Versa
lst = [1, 2, 3]
tup = tuple(lst)  
print("List to Tuple:", tup, type(tup))  # Output: (1, 2, 3) <class 'tuple'>

tup2 = (4, 5, 6)
lst2 = list(tup2)  
print("Tuple to List:", lst2, type(lst2))  # Output: [4, 5, 6] <class 'list'>

# String to List
str_val = "hello"
list_val = list(str_val)  
print("String to List:", list_val, type(list_val))  # Output: ['h', 'e', 'l', 'l', 'o'] <class 'list'>

# Boolean Conversion
print("Bool of 0:", bool(0))   # Output: False
print("Bool of 1:", bool(1))   # Output: True
print("Bool of empty string:", bool(""))  # Output: False
print("Bool of 'Python':", bool("Python"))  # Output: True

# Dictionary Conversion
lst_pairs = [('name', 'Alice'), ('age', 25)]
dict_val = dict(lst_pairs)  
print("List to Dict:", dict_val, type(dict_val))  # Output: {'name': 'Alice', 'age': 25} <class 'dict'>



# for i in range (2,21):
#     for j in range (i,i*11,i):
#         print( j )
#     print(end=" ")


maths=int(input("Enter maths marks : "))
physics=int(input("Enter marks : "))
biology=int(input("Enter  marks : "))
chemistry=int(input("Enter marks : "))
bio2=int(input("Enter  marks : "))



total_marks=maths+physics+biology+chemistry+bio2
print( "Tootal marks :" , total_marks )

percentage = total_marks/5 

print(" percenytage : " , percentage)

if (maths >=35 and physics >=35 and biology>=35 and chemistry >=35 and bio2 >=35):
    print("student passed away")
else:
    print("Student failed ")
