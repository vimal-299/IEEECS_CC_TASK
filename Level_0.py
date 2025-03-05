class node : # Node Creation
    def __init__(self, data = None):
        self.data = data 
        self.next = None
        self.prev = None

class linked_list : # Creating a doubly linked list 
    def __init__(self):
        self.head = None
        self.tail = None

    def length (self): # Finding the length of the doubly linked list
        t = 0
        x = self.head 
        while x :
            t+=1
            x = x.next
        print(t) 
        return(t)
    
    def insertion_beginning(self,data):  # Adding an element to the start of the list
        new_node = node(data) # Creating a new node which has the value that we want to append
        if not self.head : # If the list is empty the new value will become the head of the list 
            self.head = new_node
            return
        new_node.next = self.head # Else the new node will be inserted and point towards the head 
        self.head.prev = new_node
        self.head = new_node # The new node now acts as head

    def insertion_end(self,data):  # Adding an element to the end of the list
        new_node = node(data)  # Creating a new node which has the value that we want to append
        if not self.head : 
            self.head = new_node  # If the list is empty the new value will become the head of the list 
            return
        x = self.head
        while x.next :  # Else x will go to the last node of the list
            x = x.next
        x.next = new_node # The next node will now take the new value
        self.tail = x.next
        new_node.prev = x
        
    def traversal_forward(self):
        if not self.head :
            print ("The list is empty")  # If the list is empty 
            return None
        x = self.head
        while x : # Else, print the node values one by one
            print(x.data, end=" ")
            x = x.next
        print('\n')

    def traversal_backward(self):
        if not self.tail :
            print ("The list is empty") # If list is empty
            return None
        x = self.tail
        while x : # Else the node values will be printed one by one in backwards
            print(x.data , end=" ")
            x = x.prev
