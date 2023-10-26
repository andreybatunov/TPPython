class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end == None:
            return None
        else:
            removed_node = self.end
            self.end = self.end.pref
            removed_node.pref = None
            return removed_node.data

    def push(self, val):
        if self.end == None:
            self.end = Node(val)
        else:
            new_node = Node(val)
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        current_node = self.end
        if self.end == None:
            print("Stack is empty")
        else:
            while (current_node != None):
                print(current_node.data, end = " ")
                current_node = current_node.pref
                if current_node is None:
                    print("\n")

stack = Stack()
stack.push(123)
stack.push(23)
stack.push(1231)
stack.print() # 1231 23 123
print(stack.pop()) # 1231
stack.print() # 23 123



