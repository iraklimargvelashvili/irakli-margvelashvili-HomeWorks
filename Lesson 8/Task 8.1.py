text = (input("write the text: ")).lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

text_for_check = ''

for chr in text :
    if chr in alphabet :
        text_for_check += chr

if text_for_check == text_for_check[::-1] :
    print("Is palindrome")
else :
    print("Is not palindrome")