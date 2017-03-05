# Optimal Subsrting test
# Implementing KNP Algorithm
def KnuthMorrisPratt(text, pattern):

    pattern = list(pattern)

    # Shifting Table for pattern
    shifts = [1] * (len(pattern) + 1)
    j = 1
    for i in range(len(pattern)):
        while j <= i and pattern[i] != pattern[i - j]:
            j += 1
        shifts[i + 1] = j
    
    results = []
    start_index = 0
    match_len = 0

    for char in text:
        while match_len == len(pattern) or \
              match_len >= 0 and pattern[match_len] != char:
            start_index += shifts[match_len]
            match_len -= shifts[match_len]

        match_len += 1

        if match_len == len(pattern):
            results.append(start_index)

    return results

print(KnuthMorrisPratt("bababacababa", "abab"))