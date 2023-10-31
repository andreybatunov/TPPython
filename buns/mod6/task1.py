class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.__counter = 0
    
    def push(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def get(self, index):
        if index >= self.length():
            return "Недопустимый индекс!"
        count = 0
        current_node = self.head
        while count != index:
            current_node = current_node.next
            count += 1
        return current_node.data
    
    def remove(self, index):
        if index >= self.length():
            return "Недопустимый индекс!"
        count = 0
        current_node = self.head
        while count != index - 1:
            current_node = current_node.next
            count += 1
        current_node.next = current_node.next.next
    
    def insert(self, n, val):
        if n > self.length():
            print("Недопустимый индекс")
            return
        elif n == self.length():
            self.push(val)
        else:
            index = 0
            current_node = self.head
            while index != n-1:
                current_node = current_node.next
                index += 1
            inserted_node = Node(val)
            inserted_node.next = current_node.next
            current_node.next = inserted_node
        
    def length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length = length+1
            current_node=current_node.next
        return length
            
    def print(self):
        current_node = self.head
        if self.head == None:
            print("Stack is empty")
        else:
            while (current_node is not None):
                print(current_node.data, end = " ")
                current_node = current_node.next
                if current_node is None:
                    print("\n")
    
    def __iter__(self):
        self.curr = self.head
        return self
    
    def __next__(self):
        current = self.curr
        if self.__counter < self.length():
            self.curr = current.next
            self.__counter += 1
            return current.data
        else:
            raise StopIteration
        
    
mylist = LinkedList()
mylist.push(5)
mylist.push(-2)
mylist.push(12)
mylist.push(53123)
mylist.push(0)
mylist.print() # 5 -2 12 53123 0 
mylist.remove(2)
mylist.print() # 5 -2 53123 0
print(mylist.get(2)) # 53123
mylist.insert(3, 666)
mylist.print() # 5 -2 53123 666 0
for node in mylist:
    print(node, end = " ") # 5 -2 53123 666 0








