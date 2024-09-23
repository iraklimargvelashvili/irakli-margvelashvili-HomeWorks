import math

n = int(input("Write your number: "))
#count = 0
separators = ""

if(n <= 0 or n >= 1000):
    print("Please, check your number")
else:
    root = math.floor(math.sqrt(n))
    for elem in range(1,root+1):
        #print(elem)
        if(n % elem == 0):
            #count += 2
            separators += "{} {} ".format(elem,int(n/elem))
            #print(count)
    if(math.sqrt(n) == root):
        length_last_separ = len(str(int(root)))+1
        #print(length_last_separ)
        print(separators[0:-length_last_separ])
    else:
        print(separators)

