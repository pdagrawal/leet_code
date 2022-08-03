def find_numbers_with_even_number_of_digits(nums: List[int]) -> int:
    even_count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            even_count += 1
    return even_count

print(find_numbers_with_even_number_of_digits([12,345,2,6,7896]))
