# Dictionay of phone-key and list of characters pair
phone = {
	'0': [],
	'1': [],
	'2': ["a","b", "c"],
	'3': ["d","e", "f"],
	'4': ["g","h", "i"],
	'5': ["j","j", "k", "l"],
	'6': ["m","n", "o"],
	'7': ["p","q", "r", "s"],
	'8': ["t","u", "v"],
	'9': ["w","x", "y", "z"],
}

# Returns list of possible sequence of characters 
# that fit sequence input
def words(number):
	num = str(number)
	results = []
	for digit in num:
		if digit == '0' or digit == '1':
			pass
		elif results == []:
			results = phone[digit]
		else:
			solution = []
			for elem in results:
				for char in phone[digit]:
					solution.append(elem + char)
			results = solution
	return results
