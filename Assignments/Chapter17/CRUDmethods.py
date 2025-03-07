import mysql.connector
from mysql.connector import errorcode
from datetime import date

def DBConnection():
    # Establishes a database connection
    DbName = 'SP2024Python'
    try:
       conn = mysql.connector.connect(user='root',
                                 password='password',
                                 host='localhost',
                                 database=DbName)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Something wrong with username/password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
           print("Database does not exist")
        else:
           print(err)
    return conn

def Create_Table_Empl(conn):
    # Creates the Employee table if it doesn't exist
    TABLES = {}
    TABLES['Employee_Guha'] = (
        "CREATE TABLE IF NOT EXISTS `Employee_Guha` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `birth_date` date NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ")")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            crsr = conn.cursor()
            crsr.execute(table_description)
            print("Table {} created successfully".format(table_name))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table {} already exists.".format(table_name))
            else:
                print(err.msg)

def Select_Data_All(conn):
    # Selects all data from the Employee table
    query = "SELECT emp_no, first_name, last_name, gender, birth_date, hire_date FROM Employee_Guha"
    try:
        crsr = conn.cursor()
        crsr.execute(query)
        result = crsr.fetchall()
        print("\nEmployee Listing:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(err)

def Select_Data_By_EmpNo(empNo, conn):
    # Selects data from the Employee table by employee number
    query = "SELECT emp_no, first_name, last_name, gender, birth_date, hire_date FROM Employee_Guha WHERE emp_no = %s"
    try:
        crsr = conn.cursor()
        crsr.execute(query, (empNo,))
        result = crsr.fetchone()
        if result:
            print("\nEmployee with Employee Number {}:".format(empNo))
            print(result)
        else:
            print("\nEmployee not found with Employee Number {}.".format(empNo))
    except mysql.connector.Error as err:
        print(err)

def Insert_Into_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, conn):
    # Inserts a new record into the Employee table
    query = "INSERT INTO Employee_Guha (birth_date, first_name, last_name, gender, hire_date) VALUES (%s, %s, %s, %s, %s)"
    data = (DOB, Fnm, Lnm, Gender, HireDt)
    try:
        crsr = conn.cursor()
        crsr.execute(query, data)
        conn.commit()
        print("\nRecord inserted successfully.")
    except mysql.connector.Error as err:
        print(err)

def Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNbr, conn):
    # Updates an existing record in the Employee table
    query = "UPDATE Employee_Guha SET birth_date = %s, first_name = %s, last_name = %s, gender = %s, hire_date = %s WHERE emp_no = %s"
    data = (DOB, Fnm, Lnm, Gender, HireDt, empNbr)
    try:
        crsr = conn.cursor()
        crsr.execute(query, data)
        conn.commit()
        if crsr.rowcount > 0:
            print("\nRecord updated successfully.")
        else:
            print("\nNo record found with Employee Number {}.".format(empNbr))
    except mysql.connector.Error as err:
        print(err)

def Delete_Rec_From_Empl_Table(empNbr, conn):
    # Deletes a record from the Employee table
    query = "DELETE FROM Employee_Guha WHERE emp_no = %s"
    try:
        crsr = conn.cursor()
        crsr.execute(query, (empNbr,))
        conn.commit()
        if crsr.rowcount > 0:
            print("\nRecord deleted successfully.")
        else:
            print("\nNo record found with Employee Number {}.".format(empNbr))
    except mysql.connector.Error as err:
        print(err)

def Create_View(conn):
    # Creates a view named vuEmployee_Guha
    query = "CREATE OR REPLACE VIEW vuEmployee_Guha AS SELECT first_name, last_name, gender FROM Employee_Guha"
    try:
        crsr = conn.cursor()
        crsr.execute(query)
        conn.commit()
        print("\nView vuEmployee_Guha created successfully.")
    except mysql.connector.Error as err:
        print(err)

