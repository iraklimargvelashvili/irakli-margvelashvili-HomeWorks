class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def __str__(self):
        return ", ".join(map(str, self.items))


def main() :
    q = Queue()

    q.insert(1)
    q.insert(2)
    q.insert(3)

    print(q.pop())  # 1
    print(q.pop())  # 2

    print(q)

    try:
        q.pop()
        q.pop()
    except IndexError as e:
        print(e)
        
if __name__ == "__main__" :
    main()
