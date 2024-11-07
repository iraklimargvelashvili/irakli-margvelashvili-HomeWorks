from random import randint

list_1 = []
for _ in range(6) :
    list_1.append(randint(1,100))

list_2 = []
for _ in range(10) :
    list_2.append(randint(1,100))

list_3 = []
for _ in range(8) :
    list_3.append(randint(1,100))
    
    
def main() :
    print(list(map(lambda x,y,z : x+y+z, list_1, list_2, list_3)))

if __name__ == "__main__" :
    main()