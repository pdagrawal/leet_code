def sortArrayByParity(nums):
    writePointer = 0
    for i in range(len(nums)):
        if nums[i]%2 == 0:
            temp = nums[writePointer]
            nums[writePointer] = nums[i]
            nums[i] = temp
            writePointer += 1
    return nums

print(sortArrayByParity([3,1,2,4]))