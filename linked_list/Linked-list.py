# since all the methods create a new node, we don't want to write it 4 diff times
    # this class does nothing but create a node
class Node:
    
    # constructor
        # cotains a value that we will pass so it can be assigned to the node
    def __init__ (self, value):
        self.value = value
        self.next = None
    

# start with class - capitalized
class LinkedList:
    
    # constructor
    # __init__ to initalize this
        # self is always gonna be one of the parameters for constructor method
        # how we tell this is a method inside of a class instead of a function
        # value is also a param to create the first node at the time we initialize the linked list
    
    # constructor 
        # creates a new Node    
        # also initializes the new linked list
    def __init__ (self, value):
        # create a new variable new_node which uses the Node class and pass the value from this
            # constructor into that Node instance 
        new_node = Node(value)
        # brings the head in and points to the new_node
        self.head = new_node
        # brings the tail in and points to the new_node
        self.tail = new_node
        # keep track of lentgh
        self.length = 1
    
    # append 
        # create a node
        # add a node to the end
    def append (self, value):
        pass
    
    # prepend
        # create a node
        # add node to the beggining
    def prepend (self, value):
        pass
    
    # insert
        # create a node
        # insert that node to whatever index you want that
    def insert (self, value):
        pass
    
    def print_list (self):
        
        # temp is a pointer to a node (self.head), 
            # -> the node has two attibutes (value, next)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
# creating a new linked-list
    # calls the LinkedList class and pass it the number 4
my_linked_list = LinkedList(4)
print(my_linked_list.head.value) # 4