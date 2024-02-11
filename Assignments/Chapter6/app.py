tuple_data = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
list_data = [1, 3, 4, 11, 17, 28, 31, 32, 35, 40, 47]

# Calculate statistics for tuple_data
temp = 0
for i in tuple_data:
    temp += i

average = round(temp / len(tuple_data))
median = tuple_data[int(len(tuple_data) / 2)]
min_val = min(tuple_data)
max_val = max(tuple_data)
print("Tuple Data - Average =", average, " Median =", median, " Min =", min_val, " Max =", max_val)

# Calculate statistics for list_data
temp = 0
for i in list_data:
    temp += i

average = round(temp / len(list_data))
median = list_data[int(len(list_data) / 2)]
min_val = min(list_data)
max_val = max(list_data)
print("List Data - Average =", average, " Median =", median, " Min =", min_val, " Max =", max_val)
