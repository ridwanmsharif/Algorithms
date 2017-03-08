# Returns all permutations of elements using prepend algorithm
def permutation_prepend(input_list):
    if len(input_list) == 0:
	return [[]]
    else:
	list_of_lists = []
	first_char = input_list[0]
	sub_perms = permutations_prepend(input_list[1:])
	for sub_perm in sub_perms:
	    for i in range(len(sub_perm) + 1):
		result_first = sub_perm[:i]
		result_last = sub_perm[i:]
		result = result_first + [first_char] + result_last
		list_of_lists.append(result)
	return list_of_lists

# Returns all permutations of elements using insertion algorithm
def permutations_in(input_list):
    if len(input_list) == 0:
	return [[]]
    elif len(input_list) == 1:
	return [input_list]
    else:
	result = []
	for i in range(len(input_list)):
	    x = input_list[i]
	    xs = input_list[:i] + input_list[i+1:]
	    for perm in permutations_in(xs):
		result.append([x]+perm)
	return result


