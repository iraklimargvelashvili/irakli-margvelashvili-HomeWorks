from types import FunctionType
from random import randint

def max_min_sort(l:list, f:FunctionType):
    return f(l)

def main() :
    list = []
    for _ in range(100) :
        list.append(randint(10,1000000000))
        
    print("find max length number", max_min_sort(list,max))
    print("find min length number", max_min_sort(list,min))
    print("normal sortead", max_min_sort(list,sorted))
    print("reverse sorted", sorted(list, reverse=True))


if __name__ == "__main__" :
    main()