class counter_obj(object):
	"""
	counter_obj is a class that supports:
		tally_count - a class variable for total number of increments
		increment - an instance method to increment an instance variable (curr_count)
		to_string - an instance method to return the increment counter as a string
	"""

	tally_count = 0

	def __init__(self):
		"""Initializes the instance's curr_count to zero."""
		self.curr_count = 0

	def increment(self):	#O(1)
		"""Increments the instance's curr_count by one. Runs at O(1)."""
		self.curr_count += 1
		counter_obj.tally_count += 1
		return

	def to_string(self):	#O(1)
		"""Returns the instance's curr_count as a string. Runs at O(1)."""
		return str(self.curr_count)


import unittest
class test_counter(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.this_counter = counter_obj()
		cls.this_counter.increment()
		cls.this_counter.increment()
		cls.this_counter2 = counter_obj()
		cls.this_counter2.increment()
	def test_increment(self):
		self.assertEqual(self.this_counter.curr_count, 2)
	def test_tally_count(self):
		self.assertEqual(self.this_counter.tally_count, 3)
if __name__ == '__main__':
	unittest.main()
