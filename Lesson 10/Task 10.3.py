def factorial (n) :
    if type(n) != int or n < 0:
        return 'Please, choose integer'
    if n == 0 :
        return 1
    
    result = 1
    
    while n > 0 :
        result = result * n
        n -= 1
    
    return result

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(10))
    