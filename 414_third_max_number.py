def thirdMax(nums):
    nums.sort()
    first = nums[0]
    second = nums[0]
    third = nums[0]
    for num in nums:
        if num in [first, second, third]:
            continue
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
        print(first, second, third)
    return first if third == second else third

print(thirdMax([2,2,3,1]))