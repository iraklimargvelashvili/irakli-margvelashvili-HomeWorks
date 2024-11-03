from random import randint

numb_list = []

for n in range(0,30) :
    numb_list.append(randint(1,30))

result = []

for numb in numb_list :
    for n in range(0,numb) :
        result.append(numb)

print(f"List - {result} \n Length - {len(result)}")