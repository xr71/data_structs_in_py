class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_stack(stack):
    if stack.is_empty():
        return Stack()
    elif stack.size() == 1:
        return stack
    else:
        holder_stack = Stack()
        while stack.is_empty() is False:
            holder_stack.push(stack.pop())
        return holder_stack
    
test_stack = Stack()
for i in [1,2,3,4]:
    test_stack.push(i)

print(test_stack.head.data)
revs = reverse_stack(test_stack)
print(revs)
print(revs.head)
print(revs.head.data)
print(revs.head.next.data)
