import csv
def generate_key(first_name, last_name, dob):
    key = first_name[0] + last_name[:5] + dob.replace('-', '')[4:]
    return key

def main():
    input_file = 'MidTermIn.csv'
    output_file = 'MidTermOut.csv'

    with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)

        # Read the header
        header = next(reader)
        header.append('Key')
        writer.writerow(header)

        # Process each row
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            dob = row[2].replace('-', '')
            key = generate_key(first_name, last_name, dob)
            row.append(key)
            writer.writerow(row)

    print(f"Output CSV file '{output_file}' generated successfully.")

if __name__ == "__main__":
    main()
