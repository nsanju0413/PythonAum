import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

# Function to establish a connection to the database
def DBConnection() :
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

# Function to create the Employees table
def Create_Table_Empl(conn) :

    TABLES = {}
    TABLES['Employees'] = (
        "CREATE TABLE `Employees` ("
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

# Function to insert data into the Employees table
def Insert_Into_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, conn):

    Insert_stmt = ("INSERT INTO Employees "
                   "(first_name, last_name, gender, birth_date, hire_date) "
                   "VALUES (%s, %s, %s, %s, %s)")

    crsr = conn.cursor()

    new_data = (Fnm, Lnm, Gender, DOB, HireDt)

    crsr.execute(Insert_stmt, new_data)

    if crsr.rowcount == 1 :
       print("\nInsert is successful\n")
    else :
       print("\nInsert is not successful\n")

    conn.commit()

# Function to update data in the Employees table
def Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNo, conn):

    crsr = conn.cursor()

    Update_stmt = ("UPDATE Employees   \
                    SET first_name = %s, \
                    last_name = %s, \
                    gender = %s,      \
                    birth_date = %s,   \
                    hire_date = %s   \
                    WHERE emp_no  = %s" )

    new_data = (Fnm, Lnm, Gender, DOB, HireDt, empNo)

    crsr.execute(Update_stmt, new_data)

    if crsr.rowcount == 1 :
       print("\nUpdate is successful\n")
    else :
       print("\nUpdate is not successful\n")

    conn.commit()

# Function to delete data from the Employees table
def Delete_Rec_From_Empl_Table(empNo, conn):

    crsr = conn.cursor()

    Delete_stmt = ("DELETE From Employees WHERE emp_no = %s" )

    actual_data = (empNo,)   # remember comma at the end

    crsr.execute(Delete_stmt, actual_data)

    if crsr.rowcount == 1 :
       print("\nDelete is successful\n")
    else :
      print("\nDelete is not successful\n")

    conn.commit()

# Function to select all data from the Employees table
def Select_Data_All(conn):

    query = "SELECT * FROM Employees"

    crsr = conn.cursor()
    crsr.execute(query)
    result = crsr.fetchall()

    if result == "" :
       print("\nRec not found\n")
    else :
        for r in result:
            print(r)

    conn.commit()

# Function to select data from the Employees table by emp_no
def Select_Data_By_EmpNo(empNo, conn):

    query = "SELECT * FROM Employees WHERE emp_no = " + empNo

    crsr = conn.cursor()
    crsr.execute(query)
    result = crsr.fetchall()

    if result == "" :
       print("\nRec not found\n")
    else :
        for r in result:
            print(r)

    conn.commit()

# Main function to establish database connection and call CRUD operations
def main():
    conn = DBConnection()
    if conn:
        print("Database connection established successfully.")
        # Create necessary table if not exists
        Create_Table_Empl(conn)
        # Perform CRUD operations
        # Insert_Into_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, conn)
        # Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNo, conn)
        # Delete_Rec_From_Empl_Table(empNo, conn)
        # Select_Data_All(conn)
        # Select_Data_By_EmpNo(empNo, conn)
        conn.close()
    else:
        print("Failed to establish database connection.")

if __name__ == "__main__":
    main()
