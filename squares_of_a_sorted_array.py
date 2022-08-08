def squares_of_a_sorted_array(nums):
    squared = []
    for num in nums:
        squared.append(num*num)
    return sorted(squared)

print(squares_of_a_sorted_array([-4,-1,0,3,10]))
