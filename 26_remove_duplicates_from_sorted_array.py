def removeDuplicates(nums):
    # [0,0,1,1,1,2,2,3,3,4]
    index = 0
    for i in range(len(nums)):
        if index+1 == len(nums):
            break
        if nums[index] == nums[index+1]:
            nums.remove(nums[index+1])
        else:
            index += 1
    return nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
