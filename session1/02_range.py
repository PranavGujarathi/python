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

    