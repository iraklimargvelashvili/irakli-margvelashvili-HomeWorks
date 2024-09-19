speed = input("Please, write speed:")
# 30-ზე ნაკლები - slow
# 120-ზე მეტი - very fast
# 60-ზე მეტი - fast
# 30-ზე მეტია - moderate
speed = float(speed)
if(speed < 30 and speed >= 0):
    print("SLOW") 
elif(speed > 30 and speed <= 60):
    print("MODERATE")
elif(speed > 60 and speed <= 120):
    print("FAST")
elif(speed > 120):
    print("VERY FAST")
else:
    print("undefinde")
