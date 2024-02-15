import csv
with open("ch7_TestFile2Read.txt", "r") as infile:
    reader = csv.reader(infile)

    filtered_values = []
    for row in reader:
        for value in row:
            try:
                num = int(value.strip())
                if num < 50:
                    filtered_values.append(num)
            except ValueError:
                print(f"Skipping non-integer value: {value.strip()}")

with open("ch7_TestFile2Write.txt", "w") as outfile:
    for value in filtered_values:
        outfile.write(str(value) + "\n")

print("Filtered values below 50 have been stored in 'ch7_TestFile2Write.txt'.")
