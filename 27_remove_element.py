def remove_element(nums, val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)

print(remove_element([1, 2, 3, 4,3, 5,3, 6, 7, 8], 3))
