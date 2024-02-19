import csv

INPUT_FILE = "inputfile.csv"
OUTPUT_FILE = "outputfile.csv"

# with read
with open(INPUT_FILE, 'r') as filein:
    csvreader = csv.reader(filein)

    all_rows = []
    for row in csvreader:
        new_row = []
        lot_nbr = row[0].strip()
        bed_nbr = row[1].strip()
        bath_nbr = row[2].strip()
        garage_nbr = row[3].strip()  # Fixed index for garage_nbr

        if lot_nbr == "LotNbr":
            new_row.extend([lot_nbr, bed_nbr, bath_nbr, garage_nbr, "HousePrice"])
            all_rows.append(new_row)
        else:
            house_price = 25000 + (int(bed_nbr) * 20000) + (int(bath_nbr) * 15000) + (int(garage_nbr) * 10000)
            house_price_formatted = "${:,.2f}".format(house_price)
            new_row.extend([lot_nbr, bed_nbr, bath_nbr, garage_nbr, house_price_formatted])
            all_rows.append(new_row)

with open(OUTPUT_FILE, 'w', newline='') as fileout:
    csvwriter = csv.writer(fileout)
    csvwriter.writerows(all_rows)
