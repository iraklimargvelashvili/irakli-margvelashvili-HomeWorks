custom_numb = int(input("write integer more than 0, less than 10: "))

count = 1
result = ''
while count <= custom_numb :
    templ_count = 1
    row = ''
    while templ_count <= count :
        row += f'{templ_count} '
        templ_count += 1
    result += f'{row}\n'
    count += 1

reverse_result = ''
reverse_count = custom_numb - 1
while reverse_count > 0 :
    templ_count = 1
    row = ''
    while templ_count <= reverse_count :
        row += f'{templ_count} '
        templ_count += 1
    reverse_result += f'{row}\n'
    reverse_count -= 1

print(result+reverse_result)
