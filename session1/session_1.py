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


# 1 5
# 2 4
# 4 2
# 5 1

# mazha chukicah logic 
# a = int(input("Enter input: "))  # Take user input

# for i in range(1, a + 1):
#     if i == 3 and a == 3:  # Corrected condition
#         continue
#     print(i, a)  # Print values
#     a -= 1  # Decrease 'a' to generate required sequence



# for i in range(1,6):
#     print(i,6-i)

for i,j,k in zip(range(1,6), range(5,0,-1), range(1,6)):          # zip = used to take multiple range functions
    if i == 3 and j == 3:
        continue
    print(i, ' ', j, ' ', k)

    

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



name="naman"

print(name)
print(name[::-1])

if name==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")


#  vovels and consonants 

a = input("Enter string: ")  # Take input from user
vowels = 0  # Corrected spelling from 'vovels' to 'vowels'
consonants = 0  

for i in a:  # Loop through characters directly
    if i.lower() in "aeiou":  # Check for vowels (both upper and lowercase)
        vowels += 1
    elif i.isalpha():  # Ensure consonants are counted only for alphabetic characters
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


#  anagram check 
# ✅ Method 1: Using sorted() (Simple Approach)
# This method sorts both strings and compares them.

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)  # Sort and Compare

# Example Usage
print(is_anagram("listen", "silent"))  # ✅ True
print(is_anagram("hello", "world"))    # ❌ False

# ✅ Handling Case & Spaces (Real-world Use Case)
# If we want to ignore case & spaces, we preprocess the strings.

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()  # Remove spaces, convert to lowercase
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# Example Usage
print(is_anagram("Listen", "Silent"))         # ✅ True (Case insensitive)
print(is_anagram("Dormitory", "Dirty Room"))  # ✅ True (Ignores spaces)
print(is_anagram("Hello", "Ole H"))           # ❌ False


#  panagram 
# all alphabest should be prsesent in string ( 26 charecters all )



#  subtring in string 
str2 = str(input("Enter a string: "))
str3 = str(input("Enter a string: "))

new_string = str2.count(str3)
print(new_string)

# ✅ Method 1: Using count() (Best & Simplest Approach)

def count_substring(string, substring):
    return string.count(substring)  # Direct method

# Example Usage
text = "hello hello world hello"
sub = "hello"
print(count_substring(text, sub))  # Output: 3


# ✅ Method 3: Using a Manual Loop (Alternative Approach)

def count_substring_manual(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

# Example Usage
text = "abababa"
sub = "aba"
print(count_substring_manual(text, sub))  # Output: 3


str1 = str(input("enter the string RLE type vala : "))
new_str = {}

for i in range(len(str1)):
    key = str1[i]
    count = 0
    for j in range(len(str1)):
        if key == str1[j]:
            count +=1
        new_str[key] = count
print(new_str)
for i,j in new_str.items():
    print(i,j,sep='',end='')

arr=[1,2,3,4,5]

product=1
for i in arr:
    product*=i

print(product)

