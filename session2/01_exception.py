
val1 = int(input("Enter nuber"))
val2 = int(input("Enter nuber"))
print(val1 / val2)                  #  (1/0) =  ZeroDivisionError


val1 = int(input("Enter nuber"))
val2 = int(input("Enter nuber"))
try :
    print(int(val1 / val2))
except :
    print("Can not divide by zero")                 

# Handling multiple exception

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    print(a/b)
except ZeroDivisionError as message:
    print("Please ensure that you cant divide by zero = ",message)
except ValueError as message:
    print("Enter only interger value = ", message)
     


# Handling multiple different kinds of exception with single exception block

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print(message)
    

# try:
#     a = int(input("Enter first number "))
#     b = int(input("Enter second number "))
#     print(a/b)
    
# except:
#     print("This is default part of except bloack")
# except (ValueError , ZeroDivisionError) as message:          # SyntaxError: default 'except:' must be last
#     print("Enter correct number : ",message)
    

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    print(a/b)

except (ValueError, ZeroDivisionError) as message:          
    print("Enter correct number : ",message)
    
else:
    print("Everthing is OK")

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    print(a/b)

except (ValueError, ZeroDivisionError) as message:          
    print("Enter correct number : ",message)
    
finally:
    print("I will always excuted")


# NEsted try except block

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print("First excpt block = ",msg)

except ValueError as msg:
    print("Second except block = ",msg)
        

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    print(a/b)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
else:
    print("There is no errror in try block")
finally:
    print("i am finally block i alyas excuted error raise or not")


