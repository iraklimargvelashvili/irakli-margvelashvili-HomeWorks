class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("couldn't find")

    def __str__(self):
        return ", ".join(map(str, sorted(self.elements)))


def main() :
    my_inset = Inset()

    my_inset.insert(5)
    my_inset.insert(3)
    my_inset.insert(8)
    my_inset.insert(3)

    print(my_inset.member(5))  # True
    print(my_inset.member(10))  # False

    my_inset.remove(3)

    print(my_inset)

    try:
        my_inset.remove(10)
    except ValueError as e:
        print(e)
        
if __name__ == "__main__" :
    main()
