# Pair gram simple comparison between two strings
# Index of 1.0 represents a complete match
# Index of 0.0 represents no match
# Compares using unions of sets
def dice_coefficient(a,b):
    if not len(a) or not len(b): 
        return 0.0
    if a == b: 
        return 1.0
    if len(a) == 1 or len(b) == 1: 
        return 0.0
    
    a_set = [a[i:i+2] for i in range(len(a)-1)]
    b_set = [b[i:i+2] for i in range(len(b)-1)]
    
    a_set.sort()
    b_set.sort()
    
    lena = len(a_set)
    lenb = len(b_set)
    
    matches = 0
    i = 0
    j = 0
    while (i < lena and j < lenb):
        if a_set[i] == b_set[j]:
            matches += 1
            i += 1
            j += 1
        elif a_set[i] < b_set[j]:
            i += 1
        else:
            j += 1
    
    score = float(matches * 2)/float(lena + lenb)
    return score

assert(dice_coefficient("ridwan", "jishan") == 0.2)