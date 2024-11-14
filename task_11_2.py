

# იტერაციულად

def gcd_iter(a,b) :
    separator = min(a,b)
    for n in range(separator,0,-1) :
        if b % n == 0 and a % n == 0 :
            return n
        

# ევკლიდეს ალგორითმი

def gcd_evkl(a,b) :
    separator = min(a,b)
    to_divide = max(a,b)
    
    if to_divide % separator == 0 :
        return separator
    else :
        return gcd_evkl(separator, to_divide % separator)


def main() :
    first = int(input("write first number: "))
    second = int(input("write second number: "))
    
    print(f"GCD of {first} and {second} is {gcd_iter(first,second)}")
    print(f"GCD of {first} and {second} is {gcd_evkl(first,second)}")
    
if __name__ == "__main__" :
    main()
    