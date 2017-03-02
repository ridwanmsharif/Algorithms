# Encountered this Problem during a Google mock interview
# Suffice it to say, It had to make this list

seen = []

# Finds and prints the longest substring of given string that
# contains only num number of characters
def occurence(string, num):

    seen = [0]*256
    
    curr_len = 0
    curr_start = 0
    max_len = 0
    max_start = 0
    unique = 0
    
    for n,i in enumerate(string):
        
        if seen[assn_num(i)] == 0:
            unique += 1
        seen[assn_num(i)] += 1
        if unique > num:
            
            if curr_len > max_len:
                max_start = curr_start
                max_len = curr_len
            
            while seen[assn_num(string[curr_start])] > 1:
                seen[assn_num(string[curr_start])] -= 1
                curr_len -= 1
                curr_start += 1
            if seen[assn_num(string[curr_start])] == 1:
                seen[assn_num(string[curr_start])] -= 1
                unique -= 1
                curr_len -= 1
                curr_start += 1
        curr_len += 1        
    if curr_len > max_len:
        max_start = curr_start
        max_len = curr_len

    return string[max_start:max_start + max_len]

def assn_num(char):
    num = ord(char)-ord('a')
    return num