class linked_list_singly_obj(object):
	"""
	linked_list_singly_obj is a class that supports:
		add_to_head - an instance method to add a new node to the head of the linked list.
		add_to_tail - an instance method to add a new node to the tail of the linked list.
		remove_from_head - an instance method to remove the head node from the linked list.
		remove_from_tail - an instance method to remove the tail node from the linked list.
		get_length - an instance method to return the length of the linked list.
		return_values - an instance method to return the values of the linked list as an ordered python list.
	"""
	
	class node_obj(object):
		"""The node for each item contains a link to the "next" node as well as a "data" payload. If no data is passed, then payload is set to None."""
		def __init__ (self, this_data=None):
			self.next = None
			self.data = this_data
	
	def __init__(self):
		"""Initializes the instance's linked list with a root set to None."""
		self.root = None
	
	def add_to_head(self, this_data):	#O(1)
		"""Gets passed "this_data" and sets it to the head of the linked list. Runs at O(1)."""
		this_node = linked_list_singly_obj.node_obj(this_data)
		this_node.next = self.root
		self.root = this_node
		return
	
	def add_to_tail(self, this_data):	#O(n)
		"""Gets passed "this_data" and sets it to the tail of the linked list. Runs at O(n)."""
		this_new_node = linked_list_singly_obj.node_obj(this_data)
		this_node = self.root
		if this_node == None:	#edge case = empty linked list so passed data will be root
			self.root = this_new_node
		else:
			traversed_list = False
			while not traversed_list:
				if this_node.next == None:
					traversed_list = True
				else:
					this_node = this_node.next
			this_node.next = this_new_node
		return
	
	def remove_from_head(self):	#O(1)
		"""
		Removes the current head of the linked list.
		Returns None if the linked list was empty.
		Otherwise returns the data from the removed head node.
		Runs at O(1).
		"""
		if self.root == None:	#edge case = empty linked list so nothing to remove
			return None
		this_data = self.root.data
		self.root = self.root.next
		return this_data
	
	def remove_from_tail(self):	#O(n)
		"""
		Removes the current tail of the linked list.
		Returns None if the linked list was empty.
		Otherwise returns the data from the removed tail node.
		Runs at O(n).
		"""
		this_node = self.root
		if this_node == None:	#edge case = empty linked list so nothing to remove
			return None
		if this_node.next == None:	#edge case = linked list with only one node
			this_data = this_node.data
			self.root = None
			return this_data
		while this_node.next.next != None:	#find the penultimate node
			this_node = this_node.next
		this_data = this_node.next.data
		this_node.next = None
		return this_data
	
	def get_length(self):	#O(n)
		"""Returns the length of the linked list. Runs at O(n)."""
		this_len = 0
		this_node = self.root
		if this_node == None:	#edge case = empty linked list
			return this_len
		this_len += 1
		traversed_list = False
		while not traversed_list:
			if this_node.next == None:
				traversed_list = True
			else:
				this_node = this_node.next
				this_len += 1
		return this_len
	
	def return_values(self):	#O(n)
		"""
		Returns the values of the linked list in an ordered list from head to tail.
		Returns None if an empty linked list.
		Runs at O(n).
		"""
		data_list = []
		this_node = self.root
		if this_node == None:
			return data_list
		data_list.append( this_node.data )	#add the first node's data
		traversed_list = False
		while not traversed_list:
			if this_node.next == None:
				traversed_list = True
			else:
				this_node = this_node.next
				data_list.append(this_node.data)
		return data_list


import unittest
class test_linked_list_singly(unittest.TestCase):
	def setUp(self):
		self.this_list = linked_list_singly_obj()
	def test_add_to_head(self):
		self.this_list.add_to_head(5)
		self.this_list.add_to_head(4)
		self.this_list.add_to_head(3)
		self.assertEqual(self.this_list.return_values(), [3, 4, 5], 'incorrect add_to_head')
	def test_add_to_tail(self):
		self.this_list.add_to_tail(3)
		self.assertEqual(self.this_list.return_values(), [3], 'incorrect add_to_tail on empty linked list')
		self.this_list.add_to_tail(4)
		self.this_list.add_to_tail(5)
		self.assertEqual(self.this_list.return_values(), [3, 4, 5], 'incorrect add_to_tail')
	def test_remove_from_head(self):
		self.assertEqual(self.this_list.remove_from_head(), None, 'incorrect remove_from_head from empty list')
		self.this_list.add_to_tail(3)
		self.assertEqual(self.this_list.remove_from_head(), 3, 'incorrect remove_from_head from list with one element')
		self.this_list.add_to_tail(3)
		self.this_list.add_to_tail(4)
		self.assertEqual(self.this_list.remove_from_head(), 3, 'incorrect remove_from_head from list with more than one element')
	def test_remove_from_tail(self):
		self.assertEqual(self.this_list.remove_from_tail(), None, 'incorrect remove_from_tail from empty list')
		self.this_list.add_to_tail(3)
		self.assertEqual(self.this_list.remove_from_tail(), 3, 'incorrect remove_from_tail from list with one element')
		self.this_list.add_to_tail(3)
		self.this_list.add_to_tail(4)
		self.assertEqual(self.this_list.remove_from_tail(), 4, 'incorrect remove_from_tail from list with more than one element')
	def test_get_length(self):
		self.assertEqual(self.this_list.get_length(), 0, 'incorrect get_length with empty list')
		self.this_list.add_to_tail(3)
		self.assertEqual(self.this_list.get_length(), 1, 'incorrect get_length with one element list')
		self.this_list.add_to_tail(4)
		self.assertEqual(self.this_list.get_length(), 2, 'incorrect get_length with more than one element')
if __name__ == '__main__':
    unittest.main()