class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
 
def is_equal(llist1, llist2):
    current1 = llist1.head
    current2 = llist2.head
    while (current1 and current2):
        if (current1.data >= current2.data):
            return True
        current1 = current1.next
        current2 = current2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
# Append the data in last
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
a_llist = LinkedList()
l=[]
l2=[]
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    if data%5==0:
        l.append(data)
    elif data%5!=0:
        l2.append(data)
    #a_llist.append(data)
#print('The linked list: ', end = '')
a_llist.display()
print(l+l2)

  
