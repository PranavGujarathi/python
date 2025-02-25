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

