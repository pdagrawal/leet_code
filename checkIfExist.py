def checkIfExist(arr):
    lookup = {}
    for index, num in enumerate(arr):
        if ((num * 2) in lookup and index != lookup[num*2]) or ((num/2) in lookup and index != lookup[num/2]):
            return True
        else:
            lookup[num] = index
    return False

print(checkIfExist([-2,0,10,-19,4,6,-8])) # False
print(checkIfExist([7,1,14,11])) #True