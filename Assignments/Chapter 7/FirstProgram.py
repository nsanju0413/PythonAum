INPUT_FILE = "ch7_TestFile2Read.txt"
OUTPUT_FILE = "ch7_TestFile2Write.txt"

# Using read()
with open(INPUT_FILE, "r") as infile:
    all_records = infile.read().rstrip()

my_records = all_records.split('\n')

with open(OUTPUT_FILE, "w") as outfile:
    for record in my_records:
        words = record.rstrip().split(' ')
        if int(words[0]) < 50:
            print(record)
            outfile.write(record + '\n')

# Using readlines()
with open(INPUT_FILE, "r") as infile:
    all_lines = infile.readlines()

with open(OUTPUT_FILE, "w") as outfile:
    for line in all_lines:
        record = line.replace('\n', '')
        words = record.split(' ')
        for word in words:
            if int(words[0]) < 50:
                outfile.write(record + '\n')
                break

# Using readline()
with open(INPUT_FILE, "r") as infile:
    with open(OUTPUT_FILE, "w") as outfile:
        a_line = 'a'
        while a_line != '':
            a_line = infile.readline().rstrip()
            words = a_line.split(' ')
            for word in words:
                if word != '' and int(words[0]) < 50:
                    outfile.write(a_line + '\n')
                    break

print("Bye")
