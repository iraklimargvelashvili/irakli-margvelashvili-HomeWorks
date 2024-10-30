import time
from task_11_2 import gcd_evkl,gcd_iter

if __name__ == "__main__" :
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

start_iter = time.time()
gcd_iter(a,b)
finish_iter = time.time()

start_evkl = time.time()
gcd_evkl(a,b)
finish_evkl = time.time()

print(finish_iter - start_iter)
print(finish_evkl - start_evkl)