import random
import sys

# Finds the number such that (2 ^ num) is the closest smallest num to num
# Also returns the remainder factor
def find_power_rem(num):
	
	count = 0
	val = num
	rem = val % 2

	while (rem == 0):
		count += 1
		val = val/2
		rem = val % 2

	return count, val

# Checks primality of a number
# Note: Accuracy not Guaranteed, increases with number of loops
def primality(num, loops=10):
	if num < 6:
		return [False, False, True, True, False, True][num]
	elif num & 1 == 0:
		return False
	else:
		sub_one = num - 1
		s, d = find_power_rem(sub_one)

		list_a = []
		for i in range(loops):
			a = random.randint(1, min((num - 2), sys.maxint))
			list_a.append(a)

		list_r = []
        for r in range(s):
         	list_r.append(r)

		for a in list_a:

			x = pow(a, d, num)

         	if x != 1:
         		for r in list_r:

         			x = pow(x, 2, num)
         			
         			if x == 1:
         				return False
         			elif x == (num - 1):
         				a = 0;
         				break
         		if a:
         			return False
 
      	return True  # If here, probaly true
