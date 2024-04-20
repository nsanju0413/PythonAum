#!/usr/bin/env python3

import CRUDmethods as crud
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


# Main function to perform CRUD operations for Employee table
def main():
    conn = crud.DBConnection()

    # Create necessary table
    crud.Create_Table_Empl(conn)

    print("Current Listing\n")

    # Check if there are any records in the Employee table
    rtn = crud.Select_Data_All(conn)

    # If no records exist, prompt user to fill the table first
    if rtn == 0:
        input("\nFill table first by inserting records. Press Enter to continue.")
        option = 'I'
    else:
        option = input("\nEnter option (I/U/D/V): ")

    # Perform CRUD operations based on user input
    if option.upper() == "U":
        empNo = input("\nEnter EmpNo: ")
        Fnm = input("\nEnter First Name to update: ")
        Lnm = input("\nEnter Last Name to update: ")
        Gender = input("\nEnter Gender to update: ")
        DOB = input("\nEnter Date of Birth (MM/DD/YYYY) to update: ")
        HireDt = input("\nEnter Hire Date (MM/DD/YYYY) to update: ")

        updtVal = f"{Fnm.strip()},{Lnm.strip()},{Gender.strip()},{DOB.strip()},{HireDt.strip()}"
        crud.Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNo, conn)

    elif option.upper() == "D":
        empNo = input("\nEnter EmpNo to delete: ")
        crud.Delete_Rec_From_Empl_Table(empNo, conn)

    elif option.upper() == "V":
        crud.Create_View(conn)
        crud.Select_From_View(conn)

    elif option.upper() == "I":
        Fnm = input("\nEnter First Name: ")
        Lnm = input("\nEnter Last Name: ")
        Gender = input("\nEnter Gender: ")
        DOB = input("\nEnter Date of Birth (YYYY-MM-DD): ")
        HireDt = input("\nEnter Hire Date (YYYY-MM-DD): ")

        inptVal = f"{Fnm.strip()},{Lnm.strip()},{Gender.strip()},{DOB.strip()},{HireDt.strip()}"
        crud.Insert_Into_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, conn)

    else:
        print("Wrong option chosen\n")

    print()
    crud.Select_Data_All(conn)  # Re-display the table after performing operations

    conn.close()
    print("\nBye!")


if __name__ == "__main__":
    main()
