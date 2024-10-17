text = input("please, write your text: ")
result = ''

for index in range(len(text)) :
    if index % 2 is 0 and text[index] not in 'eE' :
        result += text[index]

print(result)