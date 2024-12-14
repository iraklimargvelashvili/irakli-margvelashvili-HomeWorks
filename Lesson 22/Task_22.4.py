class List_abgrade(list):
    def min(self):
        if not self:
            raise ValueError("List is empty")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("List is empty")
        return max(self)

def main() :
    list_1 = List_abgrade([10, 20, 5, 40, 15])
    list_2 = List_abgrade()
    list_3 = List_abgrade([12,12,12,12])

    print("list_1:", list_1)
    print("Minimum value:", list_1.min())
    print("Maximum value:", list_1.max())

    try:
        print(list_2.min())
    except ValueError as e:
        print(e)

    try:
        print(list_2.max())
    except ValueError as e:
        print(e)
        
    print("list_3:", list_3)
    print("Minimum value:", list_3.min())
    print("Maximum value:", list_3.max())
    
if __name__ == "__main__" :
    main()
