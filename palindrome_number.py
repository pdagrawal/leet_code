def is_palindrom(number) -> bool:
	if number < 0:
		return False

	# Solution 1:
	# return int(str(number)[::-1]) == number

	# Solution 2:
	num = str(number)
	for i in range(int(len(num)/2)):
		if num[i] != num[-i-1]:
			return False

	return True

print(is_palindrom(12345))
print(is_palindrom(12321))
print(is_palindrom(-121))
