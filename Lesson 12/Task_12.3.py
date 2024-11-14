from random import randint
# პირობაში დაკონკრეტებული არ იყო მთელი რიცხვები, მაგრამ random.uniform-ის გამოყენებას
# ეს ჯობდა ამოცანის მიზნიდან გამომდინარე

numb_list = []

for n in range(0,30) :
    numb_list.append(randint(1,30))
    
numb_list.sort()
#print(numb_list)

i = len(numb_list) - 1

while i > 0 :
    if numb_list[i] == numb_list[i-1] :
        del numb_list[i]
        
    i -= 1

print(f"List {numb_list}",'\n','\n',f"Length {len(numb_list)}")