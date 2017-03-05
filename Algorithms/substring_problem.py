def substring_test(search, pattern):
	
    search = list(search)
    pattern = list(pattern)

    curr_index_p = 0;
    start_index = 0

    matched_index = 0;
    matches = []

    start_indices = []
    for i, elem in enumerate(pattern):
	if elem == search[0]:
	    start_indices.append(i)

    for index in start_indices:
	if search == pattern[index : index + len(search)]:
	    matches.append(index)
	else:
	    pass

    return matches
