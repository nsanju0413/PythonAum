import mysql.connector
from mysql.connector import errorcode
from datetime import date


def DBConnection():
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
    TABLES = {}
    TABLES['vuEmployee_Guha'] = (
        "CREATE TABLE IF NOT EXISTS `vuEmployee_Guha` ("
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
    query = "SELECT emp_no, first_name, last_name, gender, birth_date, hire_date FROM Employee_Guha"
    try:
        crsr = conn.cursor()
        crsr.execute(query)
        result = crsr.fetchall()
        print("EmpNo    FirstName    LastName    Gender    BirthDate    HireDate")

        for row in result:
            emp_no, first_name, last_name, gender, birth_date, hire_date = row
            print(f"{emp_no:<6}   {first_name:<11}  {last_name:<10}  {gender:<7}  {birth_date}  {hire_date}")
    except mysql.connector.Error as err:
        print(err)


def Select_Data_By_EmpNo(empNo, conn):
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
    query = "INSERT INTO Employee_Guha (birth_date, first_name, last_name, gender, hire_date) VALUES (%s, %s, %s, %s, %s)"
    data = (DOB, Fnm, Lnm, Gender, HireDt)
    try:
        crsr = conn.cursor()
        crsr.execute(query, data)
        conn.commit()
        print("\nInsert is successful")
    except mysql.connector.Error as err:
        print(err)


def Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNbr, conn):
    query = "UPDATE Employee_Guha SET birth_date = %s, first_name = %s, last_name = %s, gender = %s, hire_date = %s WHERE emp_no = %s"
    data = (DOB, Fnm, Lnm, Gender, HireDt, empNbr)
    try:
        crsr = conn.cursor()
        crsr.execute(query, data)
        conn.commit()
        if crsr.rowcount > 0:
            print("\nUpdate is successful.")
        else:
            print("\nNo record found with Employee Number {}.".format(empNbr))
    except mysql.connector.Error as err:
        print(err)


def Delete_Rec_From_Empl_Table(empNbr, conn):
    query = "DELETE FROM Employee_Guha WHERE emp_no = %s"
    try:
        crsr = conn.cursor()
        crsr.execute(query, (empNbr,))
        conn.commit()
        if crsr.rowcount > 0:
            print("\nDelete is successful.")
        else:
            print("\nNo record found with Employee Number {}.".format(empNbr))
    except mysql.connector.Error as err:
        print(err)


def Create_View(conn):
    query = "CREATE OR REPLACE VIEW vuEmployee_Guha AS SELECT first_name, last_name, gender FROM Employee_Guha"
    crsr = conn.cursor()
    try:
        crsr.execute(query)
        conn.commit()
        print("\nView  created successfully")
    except mysql.connector.Error as err:
        print(err)


def Select_View_From_vuEmployee(conn):
    query = "SELECT first_name, last_name, gender FROM vuEmployee_Guha"
    crsr = conn.cursor()
    crsr.execute(query)
    result = crsr.fetchall()

    first_name = "First Name"
    last_name = "Last Name"
    gender = "Gender"
    print("\nFirstName   LastName     Gender")

    for row in result:
        first_name, last_name, gender = row
        print(f"{first_name:<12}{last_name:<12}{gender:<7}")

    if crsr.rowcount >= 1:
        print("\nSelect from view is successful\n")
    else:
        print("\nSelect from view is not successful\n")

    conn.commit()


if __name__ == "__main__":
    conn = DBConnection()
    if conn:
        Create_Table_Empl(conn)
        Select_Data_All(conn)
        conn.close()
