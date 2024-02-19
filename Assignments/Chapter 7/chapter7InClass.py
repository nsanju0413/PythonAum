import pickle
import csv

INP_FILE = "chpt7_movies.csv"
OUT_FILE = "chpt7_movies_write.csv"
OUT_FILE2 = "chpt7_fruits_write.csv"
OUT_FILE3 = "chpt7_movies.bin"

movies = [
    ["Monty Python and the Holy Grail", 1975],
    ["Cat on a Hot Tin Roof", 1958],
    ["On the Waterfront", 1954]
]

fruits = [
    ["Strawberry", "1000", "$2,200"],
    ["Apple", "500", "$1,100"],
    ["Banana", "50", "$2,100"],
    ["Pears", "500", "$3,100"]
]

# Remove unwanted characters from the fruits list
for i in range(len(fruits)):
    for j in range(len(fruits[0])):
        fruits[i][j] = fruits[i][j].replace("',", "")

# Writing from a list to CSV file
with open(OUT_FILE, "w", newline="") as file:
    writer = csv.writer(file, delimiter=",", quotechar="|")
    writer.writerows(movies)

with open(OUT_FILE2, "w", newline="") as file:
    writer = csv.writer(file, delimiter=",", quotechar="|")
    writer.writerows(fruits)

# Writing from a list to binary file
with open(OUT_FILE3, "wb") as file:
    pickle.dump(movies, file)

# Reading from CSV or binary file
with open(OUT_FILE, newline="") as file:
    reader = csv.reader(file, delimiter=",", quotechar="|")
    for row in reader:
        print(f"{row[0]} ({row[1]})")

with open(OUT_FILE3, "rb") as file:
    movie_list = pickle.load(file)
    print(movie_list)

print('')
print("Bye")
