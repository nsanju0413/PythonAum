def find_duplicates_in_tuple(num_tuple):
    tuple_dups = []
    for i in range(0, len(num_tuple)):
        for j in range(i + 1, len(num_tuple)):
            if (num_tuple[i] == num_tuple[j]):
                tuple_dups.append(num_tuple[j])

    return tuple_dups
def find_duplicates_in_list(num_list):
    list_dups = []
    for i in range(0, len(num_list)):
        for j in range(i + 1, len(num_list)):
            if (num_list[i] == num_list[j]):
                list_dups.append(num_list[j])
    return list_dups
def main():
    number_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    number_list = [4, 6, 19, 22, 26, 29, 29, 39, 42, 45, 47]
    sum_tuple = 0
    total_tuple = len(number_tuple)
    for i in range(len(number_tuple)):
        sum_tuple += number_tuple[i]
    average_tuple = sum_tuple // total_tuple
    median_tuple = len(number_tuple) // 2

    sum_list = 0
    total_list = len(number_list)
    for i in range(len(number_list)):
        sum_list += number_list[i]
    average_list = sum_list // total_list
    median_list = len(number_list) // 2

    print("TUPLE DATA : ", number_tuple)
    print("Average = ", average_tuple, "Median = ", number_tuple[median_tuple], "Minimum = ", min(number_tuple),
          "maximum = ", max(number_tuple), "Dups = ", find_duplicates_in_tuple(number_tuple))
    print()
    print("LIST DATA : ", number_list)
    print("Average = ", average_list, "Median = ", number_list[median_list], "Minimum = ", min(number_list),
          "maximum = ", max(number_list), "Dups = ", find_duplicates_in_list(number_list))

if __name__ == "__main__":
    main()
