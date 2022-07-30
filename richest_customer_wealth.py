def richest_customer_wealth(person_accounts) -> int:
	# [[1,5],[7,3],[3,5]]
	highest = 0
	for accounts in person_accounts:
		current = 0
		for account in accounts:
			current += account
		if highest < current:
			highest = current

	return highest


print(richest_customer_wealth([[1,5],[7,3],[3,5]]))
print(richest_customer_wealth([[1,2,3],[3,2,1]]))
print(richest_customer_wealth([[2,8,7],[7,1,3],[1,9,5]]))