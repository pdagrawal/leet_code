def valid_mountain_array(arr) -> bool:
    if len(arr) < 3:
        return False

    peek = arr[0]
    new_peek = False
    for i in range(1, len(arr)):
        if arr[i] == peek or (i+1 < len(arr) and arr[i] == arr[i+1]):
            return False
        elif arr[i] > peek:
            peek = arr[i]
        else:
            new_peek = True

        if new_peek and (arr[i] > arr[i-1]):
            return False

    return new_peek and peek != arr[0]

print(valid_mountain_array([1,2,3,4,9,8,7,6,5])) # true
print(valid_mountain_array([9,8,7,6,5,4,3,2,1,0])) # false
print(valid_mountain_array([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3])) # false

