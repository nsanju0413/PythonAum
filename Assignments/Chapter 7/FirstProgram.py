import csv

input_file_path = "ch7_TestFile2Read.txt"
output_file_path = "ch7_TestFile2Write.txt"

input_file = open(input_file_path, "r")

with open(output_file_path, "w") as output_file:
    line_content = 'a'
    while line_content != '':
        line_content = input_file.readline().rstrip()

        words = []
        words = line_content.split(' ')
        print(words)
        for j in range(0, len(words)):
            if words[0] != '':
                if int(words[0]) < 50:
                    output_file.write(line_content + '\n')
                    break

input_file.close()
output_file.close()
print("Bye")
