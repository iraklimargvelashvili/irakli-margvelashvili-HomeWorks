from task_11_2 import gcd_evkl

def find_lcm() :
    a = int(input("Enter a: "))
    
    if a <= 0 or a >= 10000 :
        print("please, write number 'a' more than 0, less than 10000")
        return find_lcm()
    
    b = int(input("Enter b: "))
    
    if b <= 0 or b >= 10000 :
        print("please, write number 'b' more than 0, less than 10000")
        return find_lcm()
     
    print(f"LCM of {a} and {b} is {int(a*b/gcd_evkl(a,b))}")


def main() :
    find_lcm()
    
if __name__ == "__main__" :
   main()