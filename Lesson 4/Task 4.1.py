import random

pl_num = int(input("Enter player numbers: "))
for elem in range(pl_num):
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    print(first_dice, second_dice)