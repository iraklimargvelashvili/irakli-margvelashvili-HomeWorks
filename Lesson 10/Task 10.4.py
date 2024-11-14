from math import sqrt

def is_prime_number (n) :
    if type(n) != int or n <= 0:
        return 'Please, choose a natural number'
    if n == 1 :
        return 'NO'
    
    ceil = int(sqrt(n))
    
    for numb in range(2,ceil+1) :
        if n % numb == 0 :
            return 'NO'
    
    return 'YES'

print(is_prime_number(37))
print(is_prime_number(-37))
print(is_prime_number(3.7))
print(is_prime_number(0))
print(is_prime_number(1))
print(is_prime_number(800))





