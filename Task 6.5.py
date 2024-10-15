custom_numb = int(input("write integer more than 0, less than 10: "))

count = 0
result = ''
while count <= custom_numb :
    row = ''
    templ_count = 0
    #print(templ_count)
    while templ_count <= count :
        row += f'{templ_count} '
        templ_count += 1
        reverse_count = templ_count - 1
        reverse = ''
        while reverse_count > 0 :
            reverse += f'{reverse_count} '
            reverse_count -= 1
        #print(row)
    #print(row)
    if count == 0 :
        result += (custom_numb - templ_count + 1) * '  ' + row  + (custom_numb - templ_count + 1) * '  ' + '\n'
    else :
        result += (custom_numb - templ_count + 1) * '  ' + reverse + row  + (custom_numb - templ_count + 1) * '  ' + '\n'

    count += 1
    
print(result)
