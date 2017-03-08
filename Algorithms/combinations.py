# Yielding all Combinations of k elements
def combinations_yield(k, available, used):
	if len(used) == k:
		yield list(used)
	elif len(available) == 0:
		pass
	else:
		for c in comb1(k, available[1:], used[:]+[available[0]]):
			yield c
		for c in comb1(k, available[1:], used[:]):
			yield c
print[c for c in combinations_yield(2 , 'abcde', [])]

# Returns all Combinations of k elements
def combinations_return(k, available, used):
	result = []
	if len(used) == k:
		result = result[:] + [used]
	elif len(available) == 0:
		pass
	else:
		sub = comb2(k, available[1:], used[:] + [available[0]])
		result = result[:] + sub
		sub2 = comb2(k, available[1:], used[:])
		result = result[:] + sub2
	return result

print(combinations_return(3, 'abcde', []))

