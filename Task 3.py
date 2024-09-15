numb = input("please, write your number:")

if(int(numb) < 1 or int(numb) > 10):
    print("Please, write integers from 1 to 10")

if(numb == '1'):
    print("this number არა აქვს მარტივი გამყოფი")
elif(numb == '2' or numb == '3' or numb == '5' or numb == '7'):
    print(int(numb))
elif(numb == '4' or numb == '8'):
    print(2)
elif(numb == '6'):
    print(2,3)
elif(numb == '9'):
    print(3)
elif(numb == '10'):
    print(2,5)
