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
        
    # print
    def print_list (self):
        # temp is a pointer to a node (self.head), 
            # -> the node has two attibutes (value, next)
        temp = self.head
        # while we have not reached the end of the list, we'll print temp.value
        while temp is not None:
            # prints value
            print(temp.value)
            # moves the pointer over to the next node, loop stops running when temp is None
            temp = temp.next
    
    # append 
        # create a node
        # self keyword is how we know it's a method inside of a class versus being a stand alone function
        # add a node to the end with value
    def append (self, value):
        # creates a new node and uses the Node constructor
            # passes the value that we pass the append method, the Node class will create the node
        new_node = Node(value)
        # edge case for when we don't have any item on the list, head and tail are None (is the list empty)
        if self.head is None:
            # in this situation, we'll have head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        # if there are items already existing in the linked list
        else:
            # setting the tail.next equal to the new_node
            self.tail.next = new_node
            # move the tail to point to the new node (moves over, adds the node into the list)
            self.tail = new_node
        # increase the length of the list by 1
        self.length += 1
        # optional - not necessary as a stand alone method for the append method
        return True
    
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
    

    
####                            ####
#### creating a new linked-list ####
    #### calls the LinkedList class and pass it the value of 4 to create a new node
# my_linked_list = LinkedList(4)
    #### prints the value of the head of the list
#print(my_linked_list.head.value) # 4
####

####                            ####
### adds a new node to the list ####
    #### calls the LinkedList class and pass it a value of 1 to create a new node
# my_linked_list = LinkedList(1)
    #### appends a new node and pass it the value of 2 to create a new node
# my_linked_list.append(2)
    #### prints the new list -> 1, 2
# my_linked_list.print_list()


