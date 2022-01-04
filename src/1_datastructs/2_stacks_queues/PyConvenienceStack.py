
class Stack:
    def __init__(self):
        self.arr = []
    def size(self):
        return len(self.arr)
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        if self.size() == 0:
            return None
        return self.arr.pop()
    
foo = Stack()
foo.push(1)
foo.push(2)
foo.push(42)
print(foo)
print(foo.arr)
print(foo.size())
print(foo.pop())
print(foo.arr)
print(foo.pop())
print(foo.arr)
