from random import random
from math import sqrt

numb = int(input("write your number more than 1: "))

counter = 0

for n in range(numb) :
    a = random()
    b = random()

    while a == 0 :
        a = random()

    while b == 0 :
        b = random()
        
    if sqrt(a ** 2 + b ** 2) <= 1 :
        counter += 1

print(4 * counter / numb)

# შედეგი უახლოვდება პი რიცხვს