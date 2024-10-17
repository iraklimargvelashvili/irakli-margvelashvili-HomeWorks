text = input("please, write your text: ")
vowels = 'aeiouAEIOU'
result = ''

for chr in text :
    if chr not in vowels:
        result += chr

print(result)