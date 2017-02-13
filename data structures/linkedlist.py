#basic program to create a Linkedlist

class Node(object):
	"""class to define and instantiate a Linkedlist Node"""
	# Consutructor function of Node class
	def __init__(self, data):
		self.data = data
		self.next = None


class Linkedlist(object):
	"""Class to instantiate a Linkedlist"""
	# Consutructor function of LinkedList class
	def __init__(self):
		self.head = None
		

if __name__ == "__main__":
	obj = Linkedlist()
	obj.head = Node(1)
	second = Node(2)
	third = Node(3)
	Node(1).next = second
	second.next = third
	print(obj)
	print(second.data)
	print(second.next)
	print(obj.head.data)

