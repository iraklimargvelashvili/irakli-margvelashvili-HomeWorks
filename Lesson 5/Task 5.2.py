for first in range(1,10):
    list = ""
    for second in range(1,first+1):
        if second == 2 and (first == 3 or first == 4):
            list += f"{second}*{first}={first*second}  "
        else:
            list += f"{second}*{first}={first*second} "    
    print(list)

# მე-4 და მე-5 ხაზი ემსახურება მეორე სვეტის ვიზუალურ მხარეს