# Creating my very own queue class
class queue():

    def __init__(self):
	self.head = 100
	self.tail = 99
	self.lst = [None]*100

    def push(self, elem):
	self.head -=1
	if self.head < 0:
	    self.head == 100
	self.lst[self.head] = elem
		
    def pop(self):
	value = self.lst[self.tail]
	self.tail -= 1
	if self.tail < 0:
	    self.tail == 99
	return value

# Creating my very own stack class
class stack():
	def __init__(self):
		self.lst = []

	def push(self, elem):
		self.lst.append(elem)

	def pop(self):
		if len(self.lst) == 0:
			return None
		value = self.lst[-1]
		del self.lst[-1]
		return value

# Checks whether or not string inserted is syntactically valid
# Requires: Use only parentheses characters
def is_valid(inputstr):
    s = stack()
    opening_parenthesis_map = {
	    "(": ")",
	    "[": "]",
	    "{": "}",
    }

    closing_parenthesis_map = {
    	    ")": "(",
	    "]": "[",
	    "}": "{",
    }

    result = True
    for c in inputstr:
	if opening_parenthesis_map.has_key(c):
	    s.push(c)
	else:
	    popped = s.pop()
	    result = result and closing_parenthesis_map[c] == popped
	
    result = result and len(s.lst) == 0
    return result


