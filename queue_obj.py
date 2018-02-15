class queue_obj(object):
	"""
	queue_obj is a class that creates a queue (FIFO; standing in line) and supports:
		add - an instance method to add a new node to the end of the queue.
		remove - an instance method to return the value from the first node of the queue, and remove it.
		peek - an instance method to return the value from the first node of the queue.
		isEmpty - an instance method to return True if the queue is empty, False otherwise.
		get_length - an instance method to return the length of the queue.
		return_values - an instance method to return the values of the queue as an ordered python list.
	"""
	
	class node_obj(object):
		"""The node for each item contains a link to the "next" node as well as a "data" payload. If no data is passed, then payload is set to None."""
		def __init__ (self, this_data=None):
			self.next = None
			self.data = this_data
	
	def __init__(self):
		"""Initializes the instance's stack with a root set to None."""
		self.root = None
	
	def add(self, this_data):	#O(n)
		"""Creates a new node with the added data and adds it to the end of the queue. Runs at O(n)."""
		this_new_node = queue_obj.node_obj(this_data)
		this_node = self.root
		if this_node == None:	#edge case = empty queue
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
	
	def remove(self):	#O(1)
		"""
		Returns the data payload from the first node in the queue, then removes it.
		Returns None if the queue is empty.
		Runs at O(1).
		"""
		if self.root == None:	#edge case = empty queue
			return None
		this_data = self.root.data
		self.root = self.root.next
		return this_data
	
	def peek(self):	#O(1)
		"""
		Returns the data payload of the first node in the queue.
		Returns None if the queue is empty.
		Runs at O(1).
		"""
		if self.root == None:	#edge case = empty queue
			return None
		return self.root.data
	
	def isEmpty(self):	#O(1)
		"""Returns True if the queue is empty, False otherwise. Runs at O(1)."""
		return self.root == None
	
	def get_length(self):	#O(n)
		"""Returns the length of the queue. Runs at O(n)."""
		this_len = 0
		this_node = self.root
		if this_node == None:	#edge case = empty queue
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
		Returns the values of the queue in an ordered list from first to last.
		Returns None if an empty queue.
		Runs at O(n).
		"""
		data_list = []
		this_node = self.root
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
class test_queue(unittest.TestCase):
	def setUp(self):
		self.this_queue = queue_obj()
	def test_add(self):
		self.this_queue.add(3)
		self.this_queue.add(4)
		self.this_queue.add(5)
		self.assertEqual(self.this_queue.return_values(), [3, 4, 5], 'incorrect add')
	def test_remove(self):
		self.assertEqual(self.this_queue.remove(), None, 'incorrect remove on empty queue')
		self.this_queue.add(3)
		self.assertEqual(self.this_queue.remove(), 3, 'incorrect remove on 1-element queue')
		self.this_queue.add(3)
		self.this_queue.add(4)
		self.assertEqual(self.this_queue.remove(), 3, 'incorrect remove on queue with more than 1 element')
	def test_peek(self):
		self.assertEqual(self.this_queue.peek(), None, 'incorrect peek on empty queue')
		self.this_queue.add(3)
		self.assertEqual(self.this_queue.peek(), 3, 'incorrect peek on 1-element queue')
		self.this_queue.add(4)
		self.assertEqual(self.this_queue.peek(), 3, 'incorrect peek on queue with more than 1 element')
	def test_isEmpty(self):
		self.assertEqual(self.this_queue.isEmpty(), True, 'incorrect isEmpty on empty queue')
		self.this_queue.add(3)
		self.assertEqual(self.this_queue.isEmpty(), False, 'incorrect isEmpty on filled queue')
	def test_get_length(self):
		self.assertEqual(self.this_queue.get_length(), 0, 'incorrect get_length with empty list')
		self.this_queue.add(3)
		self.assertEqual(self.this_queue.get_length(), 1, 'incorrect get_length with one element list')
		self.this_queue.add(4)
		self.assertEqual(self.this_queue.get_length(), 2, 'incorrect get_length with more than one element')
if __name__ == '__main__':
    unittest.main()