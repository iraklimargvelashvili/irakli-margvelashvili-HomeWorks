def collatz_conj_with_cash(n,*, cash = {}):
    cash[n] = [n]
    while(cash[n][-1] != 1):
        if(cash[n][-1] % 2 == 0):
            cash[n].append(int(cash[n][-1]/2))
        else:
            cash[n].append(cash[n][-1]*3+1)
    return cash[n]


def collatz_conj_normal(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1
        result.append(n)
    return result

def main():
    n = int(input("Write n: "))
    print(collatz_conj_with_cash(n))
    print(collatz_conj_normal(n))

if __name__ == "__main__" :
    main()