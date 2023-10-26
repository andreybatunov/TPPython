class Node:

    def __init__(self, data):
        self.data = data
        self.nref = None 
        self.pref = None  


class Queue:

    def __init__(self):
        self.start = None 
        self.end = None  

    def pop(self):
        if self.start is None:
            return None
        else:
            result = self.start.data
            self.start = self.start.nref
            self.start.pref = None
            return result

    def push(self, val):
        if self.end is None:
            self.start = Node(val)
            self.end = self.start
        else:
            self.end.nref = Node(val)
            self.end.nref.pref = self.end
            self.end = self.end.nref

    def insert(self, n, val):
        if n > self.length():
            print("Недопустимый индекс")
            return
        elif n == self.length():
            self.push(val)
        else:
            index = 0
            current_node = self.start
            while (index != n-1):
                current_node = current_node.nref
                index += 1
            inserted_node = Node(val)
            inserted_node.pref = current_node
            inserted_node.nref = current_node.nref
            current_node.nref.pref = inserted_node
            current_node.nref = inserted_node
        
    
    def length(self):
        current_node=self.start
        length=0
        while current_node is not None:
            length=length+1
            current_node=current_node.nref
        return length
                

    def print(self):
        current_node = self.start
        while current_node is not None:
            print(current_node.data, end =" ")
            current_node = current_node.nref
            if current_node is None:
                print("\n")
        
        
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.print() # 1 2 3 4 5
queue.insert(2,123)
queue.print() # 1 2 123 3 4 5
print(queue.pop()) # 1
queue.print() # 2 123 3 4 5
queue.insert(5, 4343)
queue.print() # 2 123 3 4 5 4343 
queue.insert(123, 1233) # Недопустимый индекс

