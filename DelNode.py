#Question Link: https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1
class Node():
	def __init__(self,val=None):
		self.data = val
		self.next = None

def push(head, val):
	newnode = Node(val)
	newnode.next = head.next
	head.next = newnode

def print_list(head):
	temp = head.next
	while(temp!=None):
		print(temp.data, end = ' ')
		temp = temp.next
	print()

def delete_node(node):
	if(node==None):
		return
	elif (node.next != None):
		node.data =  node.next.data
		node.next = node.next.next
	else:
		node=Node()	
if __name__ == '__main__':
	head = Node()
	push(head,1)
	push(head,4)
	push(head,1)
	push(head,12)
	push(head,1)

	print('list before deleting:')
	print_list(head)
	delete_node(head.next.next.next.next.next)
	print('list after deleting: ')
	print_list(head)	