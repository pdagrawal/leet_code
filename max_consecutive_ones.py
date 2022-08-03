def max_consecutive_ones(nums) -> int:
    max_count = 0
    current = 0
    start = True
    for num in nums:
        if num == 1:
            if start:
                start = False
                current = 1
            else:
                current += 1
        else:
            start = True
        if current > max_count:
            max_count = current
    return max_count

print(max_consecutive_ones([1,0,1,1,0,1]))
print(max_consecutive_ones([1,1,0,1,1,1]))
