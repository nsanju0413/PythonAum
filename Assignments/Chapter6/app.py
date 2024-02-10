tuple_data = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
list_data = [1, 3, 4, 11, 17, 28, 31, 32, 35, 40, 47]
temp = 0

for i in tuple_data:
    temp += i

median=tuple_data[(int(len(tuple_data)/2))]
min=tuple_data[0]
max=tuple_data[len(tuple_data)-1]
print("Average = ",temp / len(tuple_data)," Median = ",median, "Min =",min,"Max = ",max)