
first_numb = input("please, write first number: ")
second_numb = input("please, write separator: ")

if(int(first_numb) < 1 or int(second_numb) < 1):
    print("Please, choose positive integer numbers.")
elif(float(first_numb) % float(second_numb) == 0):
    print("{} is multiple of {}".format(first_numb,second_numb))
else:
    print("{} isn't multiple of {}".format(first_numb,second_numb))

