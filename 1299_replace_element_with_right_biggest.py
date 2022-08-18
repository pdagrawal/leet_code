def replace_element_with_right_biggest(arr):
    # Input: arr = [17,18,5,4,6,1]
    # Output: [18,6,6,6,1,-1]
    for i in range(len(arr)):
        if i+1 == len(arr):
            arr[i] = -1
            return arr
        else:
            arr[i] = max(arr[i+1:])
    return arr

print(replace_element_with_right_biggest([17,18,5,4,6,1]))
