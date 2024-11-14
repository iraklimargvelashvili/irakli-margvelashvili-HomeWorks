def convert_to_c(f) :
    return (f - 32) * 5 / 9

def convert_to_f(c) :
    return c * 9 / 5 + 32


def main() :
    f = 100
    c = 30
    print(f"{f} fahrenheit is {convert_to_c(f)} celsius")
    print(f"{c} celsius is {convert_to_f(c)} fahrenheit")

if __name__ == "__main__" :
    main()