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

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next
if __name__ == "__main__":
	# Start with the empty list
	llist = Linkedlist()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second; # Link first node with second
	second.next = third; # Link second node with the third node
	llist.printList()


##############################Linkedlist Traversal ###########################

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

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next

if __name__ == "__main__":
	# Start with the empty list
	llist = Linkedlist()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second; # Link first node with second
	second.next = third; # Link second node with the third node
	llist.printList()
