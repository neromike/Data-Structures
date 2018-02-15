class stack_obj(object):
	"""
	stack_obj is a class that creates a stack (LIFO; stack of plates) and supports:
		push - an instance method to add a new node to the head of the stack.
		pop - an instance method to return the value from the first node of the stack, and remove it.
		peek - an instance method to return the value from the first node of the stack.
		isEmpty - an instance method to return True if the stack is empty, False otherwise.
		get_length - an instance method to return the length of the stack.
		return_values - an instance method to return the values of the stack as an ordered python list.
	"""
	
	class node_obj(object):
		"""The node for each item contains a link to the "next" node as well as a "data" payload. If no data is passed, then payload is set to None."""
		def __init__ (self, this_data=None):
			self.next = None
			self.data = this_data
	
	def __init__(self):
		"""Initializes the instance's stack with a root set to None."""
		self.root = None
	
	def push(self, this_data):	#O(1)
		"""Creates a new node with the added data and adds it to the front of the stack. Runs at O(1)."""
		this_node = stack_obj.node_obj(this_data)
		this_node.next = self.root
		self.root = this_node
		return
	
	def pop(self):	#O(1)
		"""
		Returns the data payload from the first node in the stack and removes it.
		Returns None if the stack is empty.
		Runs at O(1).
		"""
		if self.root == None:	#edge case = empty stack
			return None
		this_data = self.root.data
		self.root = self.root.next
		return this_data
	
	def peek(self):	#O(1)
		"""
		Returns the data payload of the first node in the stack.
		Returns None if the stack is empty.
		Runs at O(1).
		"""
		if self.root == None:
			return None
		return self.root.data
	
	def isEmpty(self):	#O(1)
		"""Returns True if the stack is empty, False otherwise. Runs at O(1)."""
		return self.root == None
		
	def get_length(self):	#O(n)
		"""Returns the length of the stack. Runs at O(n)."""
		this_len = 0
		this_node = self.root
		if this_node == None:	#edge case = empty stack
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
		Returns the values of the stack in an ordered list from first to last.
		Returns None if an empty stack.
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
class test_stack(unittest.TestCase):
	def setUp(self):
		self.this_stack = stack_obj()
	def test_push(self):
		self.this_stack.push(5)
		self.this_stack.push(4)
		self.this_stack.push(3)
		self.assertEqual(self.this_stack.return_values(), [3, 4, 5], 'incorrect add_to_head')
	def test_pop(self):
		self.assertEqual(self.this_stack.pop(), None, 'incorrect pop on empty stack')
		self.this_stack.push(3)
		self.assertEqual(self.this_stack.pop(), 3, 'incorrect pop on 1-element stack')
		self.this_stack.push(3)
		self.this_stack.push(4)
		self.assertEqual(self.this_stack.pop(), 4, 'incorrect pop on stack with more than 1 element')
	def test_peek(self):
		self.assertEqual(self.this_stack.peek(), None, 'incorrect peek on empty stack')
		self.this_stack.push(3)
		self.assertEqual(self.this_stack.peek(), 3, 'incorrect peek on 1-element stack')
		self.this_stack.push(4)
		self.assertEqual(self.this_stack.peek(), 4, 'incorrect peek on stack with more than 1 element')
	def test_isEmpty(self):
		self.assertEqual(self.this_stack.isEmpty(), True, 'incorrect isEmpty on empty stack')
		self.this_stack.push(3)
		self.assertEqual(self.this_stack.isEmpty(), False, 'incorrect isEmpty on filled stack')
	def test_get_length(self):
		self.assertEqual(self.this_stack.get_length(), 0, 'incorrect get_length with empty list')
		self.this_stack.push(3)
		self.assertEqual(self.this_stack.get_length(), 1, 'incorrect get_length with one element list')
		self.this_stack.push(4)
		self.assertEqual(self.this_stack.get_length(), 2, 'incorrect get_length with more than one element')
if __name__ == '__main__':
    unittest.main()