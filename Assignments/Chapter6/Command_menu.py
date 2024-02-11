def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("find - Find movies by year or name")
    print("exit - Exit program")
    print()

def show_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie[0]} ({movie[1]}) @ {movie[2]}")
    print()

def add_movie(movie_list):
    movie_name = input("Name: ")
    movie_year = input("Year: ")
    movie_price = input("Price: ")
    new_movie = [movie_name, movie_year, movie_price]
    movie_list.append(new_movie)
    print(f"{movie_name} was added.\n")

def remove_movie(movie_list):
    selection = int(input("Number: "))
    if 1 <= selection <= len(movie_list):
        removed_movie = movie_list.pop(selection - 1)
        print(f"{removed_movie[0]} was deleted.\n")
        print()
    else:
        print("Invalid movie number. Please enter a valid number.\n")

def search_movies(movie_list):
    search_type = input("Search by year or name (y/n): ").lower()

    if search_type == 'y':
        user_year = input("Year: ")
        found = False
        for movie in movie_list:
            if movie[1] == user_year:
                found = True
                print(movie[0])
        if not found:
            print("No movies found for that year.")

    elif search_type == 'n':
        user_name = input("Name: ")
        found = False
        for movie in movie_list:
            if user_name.lower() in movie[0].lower():
                found = True
                print(movie[0])
        if not found:
            print("No movies found with that name.")

    else:
        print("Invalid search type. Please enter 'y' for year or 'n' for name.")
        print()

def main():
    movie_list = [["Monty Python and the Holy Grail", "1975", "12.95"],
                  ["On the Waterfront", "1954", "9.95"],
                  ["Cat on a Hot Tin Roof", "1958", "7.95"]]
    display_menu()
    while True:
        user_command = input("Command: ")
        if user_command.lower() == "list":
            show_movies(movie_list)
        elif user_command.lower() == "add":
            add_movie(movie_list)
        elif user_command.lower() == "del":
            remove_movie(movie_list)
        elif user_command.lower() == "find":
            search_movies(movie_list)
        elif user_command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
