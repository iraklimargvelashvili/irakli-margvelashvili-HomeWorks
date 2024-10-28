numb = int(input("write your number more than 1: "))

result = 0

if numb < 1 :
    print('Check your number!')
else :
    for n in range(1,numb+1) :
        if n % 2 == 1 :
            result += 1 / (2 * n - 1)
        else :
            result -= 1 / (2 * n - 1)


print(result * 4)

# შედეგი უახლოვდება პი რიცხვს