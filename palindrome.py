class Deque():
	"""Implementation of the deque ADT"""
	def __init__(self):
		self.items = []

	def is_empty(self):
		if self.items == []:
			return True
		else:
			return False

	def add_front(self, item):
		self.items.append(item)

	def add_rear(self, item):
		self.items.insert(0, item)

	def remove_rear(self):
		return self.items.pop(0)

	def remove_front(self):
		return self.items.pop()

	def size(self):
		return len(self.items)
def palindrome(text):
	chars = dst.Deque()

	for char in text:
		chars.add_rear(char)
	palindrome_check = True
	print(chars.size())

	while chars.size() > 1 and palindrome_check:
		front_char = chars.remove_front()
		rear_char = chars.remove_rear()
		print(f"{front_char} -- {rear_char}")

		if front_char != rear_char:
			palindrome_check = False
	return palindrome_check

print(palindrome("Flase"))