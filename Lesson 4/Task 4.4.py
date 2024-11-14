n = int(input("Please, write number: "))

if(n <= 0 or n >=20):
    print("write correct number")
else:
    start = 0
    first = 1
    current = None
    result = None

    for elem in range(n):
        result = first
        current = start + first
        start = first
        first = current
    print(result)

