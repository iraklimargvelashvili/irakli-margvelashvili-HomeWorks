def count_vowels (text) :
    count = 0
    vowels = 'aeiou'
    for char in text :
        if char in vowels :
            count += 1
    return count

print(count_vowels('aaa'))
print(count_vowels('Love is freedom'))
print(count_vowels('bgnhry'))