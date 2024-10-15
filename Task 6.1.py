import random

custom_numb = int(input("write integer from 0 to 100: "))
rand_int = random.randint(0,100)

try_count = 10

while try_count > 0 :
    if custom_numb == rand_int :
        break
    elif custom_numb > rand_int :
        print("high")
        custom_numb = int(input(f"write lower integer than {custom_numb}: "))
    else :
        print("low")
        custom_numb = int(input(f"write hiegher integer than {custom_numb}: "))
    try_count -= 1

if try_count == 0 :
    print("Computer is winner")
else :
    print("You are winner!")