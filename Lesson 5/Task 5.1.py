n = int(input("Write the number: "))
result = ""

if n <= 0 or n >= 50:
    print("Write integer more, than 0 less than 50")
else:
    for _int in range(1,n+1):
        count = 3
        result += f'\n{_int} - '
        for separator in range(1,_int+1):
            if _int % separator == 0:
                if count == 0:
                    break
                count -= 1
                result += f'{separator} '
            
print (result)
