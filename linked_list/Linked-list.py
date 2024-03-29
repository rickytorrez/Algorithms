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
        
    # pop
        # creates two new variables temp & pre
        # iterates through the list and removes the last node
    def pop (self):
        # edge case for when we have an empty linked list or if we only have one node in the list
        if self.length == 0:
            return None
        # next case is if we have two or more items in the linked list
            # we'll add two variables, temp and pre
        temp = self.head
        pre = self.head
        
        # walk through the linked list with a while loop -> while temp.next is true or while it's pointing to a node
            # becomes false when at the end of a list when the pointer becomes None
        while(temp.next): 
            pre = temp
            temp = temp.next
        # points tail to the pre variable when while loop stops
        self.tail = pre
        # remove the last node, sets next on the tail to None
        self.tail.next = None
        # decrement the length by 1
        self.length -= 1
        # edge case for when we only have one node
            # since we decrement from 1 -> 0, we set the head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
        # returns the node that we just removed
            # for testing purposes, you can return temp.value instead of the whole node
        return temp.value
    
    # prepend
        # add a node at the beginning
        # pass in a value
    def prepend (self, value):
        # create node with value
        new_node = Node(value)
        # if empty list
        if self.length == 0:
            # have head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        # if list is not empty
        else:
            # have the new node point next to the head
            new_node.next = self.head
            # once head has been set, have it point to the new node 
            self.head = new_node
        # increase the length of the list by 1
        self.length += 1
        # optional
        return True
        
    # pop first
        # pops the first node of a list
    def pop_first (self):
        # if we have zero items on the list
        if self.length == 0:
            # return none
            return None
        # create a variable temp that will point to the head
        temp = self.head
        # point the head to self.head.next
        self.head = self.head.next
        # remove the pointer, set next equal no None for temp
        temp.next = None
        self.length -= 1
        # if we have zero items on the list after we decremented the length by 1
        if self.length == 0:
            # set the tail to none
            self.tail = None
        # return the item we removed from the list - temp.value should not returned, only temp
        return temp
    
    # get
        # pass in an index that returns the node at that index
    def get(self, index):
        # check to have a valid index
            # if index is less than 0 or index is greater than or equal to the length
        if index < 0 or index >= self.length:
            # return None sine we can't get a node at any of those indexes
            return None
        # create a variable called temp and set it equal to the head
        temp = self.head
        # whatever the index is, we will need temp that many times over
            # create a for loop that will run that number of times and get us to the correct node
        for _ in range(index):
            temp = temp.next
        # once for loop iterates to the index that we pass, we return the node
        return temp
        
    # set
        # pass in an index and value to change on a specific node
    def set_value (self, index, value):
        # use the get method to have temp point to the appropiate node
            # get will either get None for invalid index or a node
        temp = self.get(index)
        # test to see if temp has any value -> if temp is not None
        if temp:
            # update temp value to the value passed in this method
            temp.value = value
            # return True
            return True
        # if the get method returns None - invalid index
        return False
    
    # insert
        # create a node
        # insert that node to whatever index you want that
    def insert (self, index, value):
        # out of range
        # cant have anything that is out of bounds - ie: index < 0 or index > self.length
        if index < 0 or index >= self.length:
            # return false if not successful
            return False
        # adding to beggining - if index is at initial node, use the created prepend method to add the value to that node
        if index == 0:
            # once prepend method runs, be done
            # run this on this particular instance of the linked list (self)
            return self.prepend(value)
        # adding to the end - if the index is equal to the length, add the value to the end of the the list 
        if index == self.length:
            # once append method runs, be done
            return self.append(value)
        # adding to the somewhere in the middle
        # creates a new node
        new_node = Node(value)
        # creates the temp variable which is equal to index - 1 to point to the appropiate node
            # index - 1 needs to point to the new node in order to insert it
        temp = self.get(index - 1)
        # sets the pointer of the new node to temp.next
        new_node.next = temp.next
        # sets temp.next to point to the new_node
        temp.next = new_node
        # increment list by 1
        self.length += 1
        # return true if successful
        return True
        
    
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
    #### appends a new node and pass it the value of 2 
# my_linked_list.append(2)
    #### prints the new list -> 1, 2
# my_linked_list.print_list()
####

####                            ####
# removes the last node on a list ##
    ### creates a linked list with a node of value 1
# my_linked_list = LinkedList(1)
    ### adds a new node and pass it the value of 2
# my_linked_list.append(2)
    ### (2) Items  - pops and returns Node 2
# print(my_linked_list.pop())
    ### (1) Item - pops and returns Node 1
# print(my_linked_list.pop())
    ### (0) Items - pops and returns Node 0
# print(my_linked_list.pop())

####                            ####
# add node to the bef of the list ##
    ### creates a linked list with a node of value 2
# my_linked_list = LinkedList(2)
    ### adds a new node and pass it the value of 3
# my_linked_list.append(3)
    ### prints the list -> 2, 3
# my_linked_list.print_list()
    ### adds a new node to the beginning and pass it the value of 4
# my_linked_list.prepend(4)
    ### prints the list -> 4, 2, 3 
# my_linked_list.print_list()

####                            ####
# remove the first node from list ##
    ### creates a linked list with a node of value 2
# my_linked_list = LinkedList(2)
    ### adds a new node and pass it the value of 1
# my_linked_list.append(1)
    ### prints the list -> 2, 1
# my_linked_list.print_list()
    ### (2) Items - Returns  2 Nodes
# print(my_linked_list.pop_first())
    ### (1) Items - Returns  1 Nodes
# print(my_linked_list.pop_first())
    ### (0) Items - Returns None
# print(my_linked_list.pop_first())

####                            ####
###### get a node from list ########
    ### creates a linked list with a node of value 0
# my_linked_list = LinkedList(0)
    ### adds a new node and pass it the value of 1
# my_linked_list.append(1)
    ### adds a new node and pass it the value of 2
# my_linked_list.append(2)
    ### adds a new node and pass it the value of 3
# my_linked_list.append(3)
    ### gets the node at index 2
# print(my_linked_list.get(2))

####                            ####
###### get a node from list ########
    ### creates a linked list with a node of value 11
# my_linked_list = LinkedList(11)
    ### adds a new node and pass it the value of 3
# my_linked_list.append(3)
    ### adds a new node and pass it the value of 23
# my_linked_list.append(23)
    ### adds a new node and pass it the value of 7
# my_linked_list.append(7)
    ### sets the value on the 2 index to 4
# print(my_linked_list.set_value(1, 4))
    ### prints the list with updated value at index of 1
# my_linked_list.print_list()

####                            ####
##### insert node to a list ########
    ### creates a linked list with a node of value 0
my_linked_list = LinkedList(0)
    ### adds a new node and pass it the value of 3
my_linked_list.append(2)
    ### prints the list with updated value at index of 1
my_linked_list.print_list()
    ### inserts a value of 1 into index of 1
my_linked_list.insert(1, 1)
    ### prints the list with updated value at index of 1
my_linked_list.print_list()

