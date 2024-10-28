def reverse_text (text) :
    if type(text) != str :
        return 'Please, write string.'
    return text[::-1]

print(reverse_text('abgd'))
print(reverse_text('abgd 19 oiw'))
print(reverse_text('   '))
print(reverse_text(True))