seen = []

# Prduces the length of the longest Substring
# thats comprised of just unique characters
def max_diff(string):

    seen = [0]*256
    
    
    curr_start = 0
    max_start = 0
    unique = 0
    max_unique = 0
    
    for n,i in enumerate(string):
    	if seen[assn_num(i)] == 0:
    		
    		unique += 1 
    	else:
    		if unique > max_unique:
    			max_unique = unique
    		while unique > 1:
    			if seen[assn_num(string[curr_start])] == 1:
    				unique -= 1
    				seen[assn_num(string[curr_start])] -= 1 
    				curr_start += 1
    			else:
    				seen[assn_num(string[curr_start])] -= 1 
    				curr_start += 1
    	seen[assn_num(i)] += 1
    	if unique > max_unique:
    		max_unique = unique

    return max_unique

def assn_num(char):
    num = ord(char)-ord('a')
    return num