class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Stack: [" + ", ".join(map(str, reversed(self.items))) + "]"

def main() :
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)

    print("Peek:", stack.peek())

    print("Popped:", stack.pop())
    print(stack)

    print("Is Empty:", stack.is_empty())

    print("Size:", stack.size())

    stack.pop()
    stack.pop()
    print("Is Empty after popping all:", stack.is_empty())

    try:
        stack.pop()
    except IndexError as e:
        print(e)
        
if __name__ == "__main__" :
    main()
