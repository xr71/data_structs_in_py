# our stack class should have the following functionalities
## push, pop, size, top, is_empty
#

class Stack:
    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, val):

        if self.next_index == len(self.arr):
            self._handle_full_capacity()

        self.arr[self.next_index] = val
        self.next_index += 1
        self.num_elements += 1

    def _handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [ None for _ in range(2 * len(old_arr)) ]
        for idx,elem in enumerate(old_arr):
            self.arr[idx] = elem

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.num_elements == 0:
            self.next_index = 0
            return None
        self.num_elements -= 1
        self.next_index -= 1
        popped_elem = self.arr[self.next_index]
        self.arr[self.next_index] = None
        return popped_elem



mystack = Stack()
print(mystack.size())
print(mystack.is_empty())
mystack.push("fish")
mystack.push(42)
mystack.push(1)
print(mystack.size())
print(mystack.is_empty())
print(mystack.arr)
print()
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print()
print(mystack.size())
print(mystack.is_empty())
print(mystack.arr)
