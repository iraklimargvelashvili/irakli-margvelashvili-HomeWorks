import random

n = int(input("Write positive integer: "))
max_numb = 0

if(n <= 0 or n >= 30):
    print("Please, check your number")
else:
    for elem in range(n):
        rand_numb = random.randint(0,1000)
        if(max_numb < rand_numb):
            max_numb = rand_numb
        #print(rand_numb)
        #print(max_numb)
    print(max_numb)
