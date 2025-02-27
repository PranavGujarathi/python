# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()


# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     for j in range(1,n+2-i):
#         print(n+1-j,end=" ")
#     print()


# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-i),end=" ")5
#     print()


# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print(" "(n-i),""*i,end=" ")
#     print()


# import time
# n = int(input("Enterthe number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()


# import time
# n = int(input("Enterthe number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


n=int(input("Enter n : "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()
