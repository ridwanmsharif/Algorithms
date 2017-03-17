# Returns all permutations of elements using prepend algorithm
def permutation_prepend(input_list):
    if len(input_list) == 0:
	return [[]]
    else:
	list_of_lists = []
	first_char = input_list[0]
	sub_perms = permutation_prepend(input_list[1:])
	for sub_perm in sub_perms:
	    for i in range(len(sub_perm) + 1):
		result_first = sub_perm[:i]
		result_last = sub_perm[i:]
		result = result_first + [first_char] + result_last
		list_of_lists.append(result)
	return list_of_lists

# Check if Sorted
def is_sorted(input_list):
	i = 1
	while (i < len(input_list)):
		if input_list[i-1] > input_list[i]:
			return False
		i += 1
	return True

def bogosort(input_list):
	list_of_lists = permutation_prepend(input_list)
	for lst in list_of_lists:
		if is_sorted(lst):
			return lst

print(bogosort([9, 8, 7, 6, 5, 4, 3, 2, 1]))

