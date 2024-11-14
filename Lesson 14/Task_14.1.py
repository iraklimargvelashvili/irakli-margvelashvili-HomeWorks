import math
temperature_tuple = ((33,34,28),(24,31,27),(24,23,27),(28,32,34),(33,21,28),(20,25,31),(21,31,28))

t = ((1,2,3),(10,11,12))

min_temp =  tuple(map(min,temperature_tuple))
max_temp = tuple(map(max,temperature_tuple))
average_temp = tuple(map(lambda x: round(sum(x)/3,2),temperature_tuple))
week_average = round(sum(average_temp)/len(average_temp),2)

print("min temperature on ich day is:", min_temp)
print("max temperature on ich day is:", max_temp)
print("average temperature on ich day is:", average_temp)
print("average temperature in week is:", week_average)