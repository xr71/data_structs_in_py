
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

def is_balanced_parentheses(instr: str) -> bool:

    if instr == "" or instr is None:
        return False

    _stack = Stack()
    for c in instr:
        if c == "(":
            _stack.push(c)
        if c == ")":
            if _stack.pop() is None:
                return False
            else:
                continue
    
    if _stack.size() == 0:
        return True
    else:
        return False


print(is_balanced_parentheses("(x+1)"))
print(is_balanced_parentheses("((x+1)"))
print(is_balanced_parentheses("(x+1))"))
print(is_balanced_parentheses("()"))
print(is_balanced_parentheses("("))
print(is_balanced_parentheses(""))
