def solution(sequence):
	if len(sequence) < 3:
		return True

	check = apply_check(sequence, False)
	return check

def apply_check(asequence, removed):
	print(asequence)
	print(removed)
	flag = True
	for i in range(len(asequence) - 1):
		print(asequence[i])
		if (asequence[i] > asequence[i + 1]) and not removed:
			print('inside recursion')
			sublist = list(asequence)
			sublist.pop(i)
			print('sublist', sublist)
			removed = True
			apply_check(sublist, removed)
		elif (asequence[i] > asequence[i + 1]) and removed:
			print('Inside output')
			flag = False
			break

	return True

print('Calling method')
output = solution([1,3,2,5,4,10])

print('Output: ', output)