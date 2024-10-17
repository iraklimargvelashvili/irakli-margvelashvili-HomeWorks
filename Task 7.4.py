text = input("please, write your text: ")
choice = input("if you want encript, write 'e', either - 'd':  ")

result = ''

line_encr = 'qwertyuiopqasdfghjklazxcvbnmz'
line_decr = 'zmnbvcxzalkjhgfdsaqpoiuytrewq'

for chr in text :
    if choice == 'e' and chr in line_encr :
        curr_index = line_encr.find(chr)
        result += line_encr[curr_index + 1]
    elif choice == 'd' and chr in line_decr :
        curr_index = line_decr.find(chr)
        result += line_decr[curr_index + 1]
    else :
        result += chr

print(result)