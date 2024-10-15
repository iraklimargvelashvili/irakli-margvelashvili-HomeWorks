custom_numb = int(input("write integer from 0 to 10000: "))
revers_numb = ''
sum = 0

while custom_numb >= 1 :
    last_chr = custom_numb % 10
    leftover_part = int((custom_numb - last_chr) / 10)
    revers_numb += f'{last_chr}'
    sum += last_chr
    custom_numb = leftover_part

print(str(revers_numb),sum)