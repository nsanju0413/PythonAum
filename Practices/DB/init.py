def Create_Table_Empl(conn):
    TABLES = {}

    TABLES['EmployeesPY'] = (

        "CREATE TABLE `EmployeesPY` ("

        " `emp_no` int(11) NOT NULL AUTO_INCREMENT,"

        " `birth_date` date NOT NULL,"

        " `first_name` varchar(14) NOT NULL,"

        " `last_name` varchar(16) NOT NULL,"

        " `gender` enum('M','F') NOT NULL,"

        " `hire_date` date NOT NULL,"

        " PRIMARY KEY (`emp_no`)"

        ")")

    for table_name in TABLES:

        table_description = TABLES[table_name]

        try:

            print("Creating table {}: ".format(table_name), end='')

            crsr = conn.cursor()

            crsr.execute(table_description)

        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:

                print("already exists.")

            else:

                print(err.msg)

            print()

        else:

            print("OK")