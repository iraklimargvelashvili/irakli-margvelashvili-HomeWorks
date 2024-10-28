text = input("please, write your text: ")
result = ''
count = 5

length = len(text)

while count > 0 :
    if length < 3 :
        result += text
    elif length % 2 == 0 :
        result += text[0] + text[int(length / 2 - 1)] + text[int(length / 2)] + text[length - 1]
    else :
        result += text[0] + text[int((length - 1) / 2)] + text[length - 1]
    
    count -= 1

print(result)