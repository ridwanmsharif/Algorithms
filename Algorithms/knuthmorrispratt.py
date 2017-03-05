def knuthmorrispratt(search, pattern):
	
    search = list(search)
    pattern = list(pattern)

    curr_index = 0;
    start_index = 0

    matches = []

    start_indices = []
    for i, elem in enumerate(pattern):
        if ((curr_index < len(search)) and
            (elem != search[curr_index])):

            curr_index = 0
        elif curr_index < len(search): 
            if curr_index == 0:
                start_index = i

            if curr_index == (len(search) - 1):
                matches.append(start_index)
                curr_index = 0
            else:
                curr_index += 1

    return matches
