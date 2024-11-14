# ნაძვის ხის სიგრძეში * არ შემიყვანია, ის ვარსკვლავად ჩავთვალე
hight = int(input("Write Christmas tree hight: "))
christ_tree = ""

if(hight <= 0 or hight >= 50):
    print("Please, write number more, than 0 and less, than 50")
else:
    empty_space_for_star = ""
    tree = "*"
    for _ in range(hight+2):
        empty_space_for_star += ' ' 
    tree = f"{empty_space_for_star}{tree}{empty_space_for_star}\n"
    for grow in range(1,hight+1):
        empty_space = ""
        floor = ""
        sticks = "|"
        for _ in range(grow - 1):
            sticks += '||'
        for _ in range(hight+1 - (grow - 1)):
            empty_space += ' '
        floor = f"{empty_space}/{sticks}\\{empty_space}\n"
        tree += floor
    print(tree)