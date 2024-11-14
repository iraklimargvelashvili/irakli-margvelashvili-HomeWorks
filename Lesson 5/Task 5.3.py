n = int(input("Write non negative integer: "))

if n < 0 or n >= 20:
    print("write the number from 0 till 20")
else:
    result = "0"
    befor = 0
    current = 1
    after = None

    while n > 0:
        result = result + f" {current}"
        after = befor + current
        befor = current
        current = after
        n -= 1

    print(result)