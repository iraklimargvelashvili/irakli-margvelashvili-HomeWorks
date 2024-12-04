small = ""
high = ""

with open("data.txt", "r") as file:
    for line in file:
        if int(line.split(",")[3]) < 10:
            small += line + "\n"
        else:
            high += line + "\n"

with open("small.txt", "w") as file:
    file.write(small)

with open("high.txt", "w") as file:
    file.write(high)

    