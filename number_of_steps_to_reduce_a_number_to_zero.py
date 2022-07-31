def number_of_steps_to_reduce_a_number_to_zero(num):
	steps = 0
	while num != 0:
		if num % 2 == 0:
			num /= 2
		else:
			num -= 1
		steps += 1

	return steps


print(number_of_steps_to_reduce_a_number_to_zero(14))
print(number_of_steps_to_reduce_a_number_to_zero(8))
print(number_of_steps_to_reduce_a_number_to_zero(123))