import CRUDmethods as crud
import mysql.connector
from mysql.connector import errorcode
from datetime import date

def main():
    conn = crud.DBConnection()

    crud.Create_Table_Empl(conn)

    print("Current Employee Listing\n")
    crud.Select_Data_All(conn)

    option = input("\nEnter option (I/U/D/V): ").upper()

    if option == "U":
        empNo = int(input("\nEnter Employee Number: "))
        Fnm = input("\nEnter First Name: ")
        Lnm = input("\nEnter Last Name: ")
        Gender = input("\nEnter Gender: ")
        DOB = input("\nEnter Date of Birth (yyyy-mm-dd): ")
        HireDt = input("\nEnter Hire Date (yyyy-mm-dd): ")
        crud.Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNo, conn)

    elif option == "D":
        empNo = int(input("\nEnter Employee Number: "))
        crud.Delete_Rec_From_Empl_Table(empNo, conn)

    elif option == "V":
        crud.Create_View(conn)
        print("View created successfully.")

    elif option == "I":
        Fnm = input("\nEnter First Name: ")
        Lnm = input("\nEnter Last Name: ")
        Gender = input("\nEnter Gender: ")
        DOB = input("\nEnter Date of Birth (yyyy-mm-dd): ")
        HireDt = input("\nEnter Hire Date (yyyy-mm-dd): ")
        crud.Insert_Into_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, conn)

    else:
        print("Wrong option chosen\n")

    print()
    print("Updated Employee Listing\n")
    crud.Select_Data_All(conn)

    conn.close()

    print("\nBye!")