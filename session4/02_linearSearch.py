
def linearSearch(inputList,element):
    for index,value in enumerate(inputList):
        if value == element:
            return index

    return -1



inputList=[1,2,3,4,5,6]
element=4

print("Index : " , linearSearch(inputList,element))