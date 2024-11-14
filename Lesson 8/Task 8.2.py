'''
პირობა ისე გავიგე, რომ შემოსული ორი სტრინგიდან, ერთიდანაც
უნდა შეიძლებოდეს მეორის მიღება და მეორედანაც პირველის მიღება;
ცარიელი ადგილებიც ითვლება
'''

str_1 = (input("write first string: ")).lower()
str_2 = (input("write second string: ")).lower()

result = 'YES'

if len(str_1) != len(str_2) :
    result = 'NO'
else :
    for chr in str_1 :
        if str_1.count(chr) != str_2.count(chr):
            result = 'NO'
    

print(result)