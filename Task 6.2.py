custom_numb = int(input("write positive integer <= 1000: "))
print(custom_numb)
result = f'{custom_numb}' + ' -> '

while custom_numb != 2 :
    if custom_numb % 2 == 0 :
        custom_numb /= 2
        result += f'{int(custom_numb)}' + ' -> '
    else :
        custom_numb = custom_numb * 3 + 1
        result += f'{int(custom_numb)}' + ' -> '

print(result + '1')