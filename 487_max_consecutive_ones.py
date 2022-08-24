def findMaxConsecutiveOnes(nums):
    first_counter = 0
    second_counter = 0
    flipped = False
    max_len = 0
    for i in range(len(nums)):
        if nums[i] == 0 and not flipped:
            flipped = True
            first_counter += 1
            second_counter = 0
        elif nums[i] == 0 and flipped:
            first_counter = second_counter + 1
            second_counter = 0
        else:
            first_counter += 1
            second_counter += 1
        if max_len < first_counter:
            max_len = first_counter
    return max_len

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
