def find_max (*numbers) :
    if len(numbers) == 0:
        return 'You have not entered numbers'
    return max(numbers)

print(find_max(1,60,2,3,4,5,19))
print(find_max(-2.9,-9.7,-10))
print(find_max())