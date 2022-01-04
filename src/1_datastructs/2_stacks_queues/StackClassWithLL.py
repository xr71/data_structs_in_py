# creating a Stack class with linked lists


class Node:
    # a node has a value and a next pointer
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, val):
        new_node = Node(val)
        # if the current stack is empty
        # we can directly attach it to the head
        # otherwise we need to shift the head and repoint
        if self.head is None:
            self.head = new_node
            self.num_elements += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.num_elements += 1
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        # check if stack is empty
        # if it is return None
        if self.head is None:
            return None
        else:
            popped_elem = self.head
            self.head = popped_elem.next
            self.num_elements -= 1

            return popped_elem.value


foo = Stack()
foo.push(1)
foo.push(2)
foo.push(42)
print(foo.head)
print(foo.head.value)
print(foo.head.next)
print()
print(foo.head.next.value)
print(foo.num_elements)
print()
print(foo.pop())
print(foo.pop())
print(foo.pop())
print(foo.pop())
print(foo.pop())
print(foo.pop())
print()
print(foo.size())
print(foo.is_empty())
print(foo.num_elements)
