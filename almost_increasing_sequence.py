def solution(sequence):
	if len(sequence) < 3:
		return True

	check = apply_check(sequence, False)
	return check

def apply_check(asequence, removed):
	for i in range(len(asequence) - 1):
		if (asequence[i] >= asequence[i + 1]) and not removed:
			sublist = list(asequence)
			if i > 0 and asequence[i-1] >= asequence[i + 1]:
				sublist.pop(i+1)
			else:
				sublist.pop(i)
			removed = True
			return apply_check(sublist, removed)
		elif (asequence[i] >= asequence[i + 1]) and removed:
			return False

	return True

print('Calling method')
print(solution([1, 2, 3, 4, 3, 6]))
print(solution([10, 1, 2, 3, 4, 5]))

