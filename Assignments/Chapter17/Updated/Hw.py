import CRUDmethods as crud
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

def main():
    conn = crud.DBConnection()

    crud.Create_Table_Empl(conn)

    print("\nCurrent Listing\n")
    crud.Select_Data_All(conn)

    option = input("\nEnter option (I/U/D/V): ")

    if option.upper() == "U":
        empNo = input("\nEnter Employee Number: ")
        Fnm = input("\nEnter First Name: ")
        Lnm = input("\nEnter Last Name: ")
        Gender = input("\nEnter Gender: ")
        DOB_str = input("\nEnter Date of Birth (mm/dd/yyyy): ")
        DOB = datetime.strptime(DOB_str, "%m/%d/%Y").date()
        HireDt_str = input("\nEnter Hire Date (mm/dd/yyyy): ")
        HireDt = datetime.strptime(HireDt_str, "%m/%d/%Y").date()
        crud.Update_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, empNo, conn)

    elif option.upper() == "D":
        empNo = input("\nEnter Employee Number: ")
        crud.Delete_Rec_From_Empl_Table(empNo, conn)

    elif option.upper() == "V":
        crud.Select_View_From_vuEmployee(conn)

    elif option.upper() == "I":
        Fnm = input("\nEnter First Name: ")
        Lnm = input("\nEnter Last Name: ")
        Gender = input("\nEnter Gender: ")
        DOB_str = input("\nEnter Date of Birth (mm/dd/yyyy): ")
        DOB = datetime.strptime(DOB_str, "%m/%d/%Y").date()
        HireDt_str = input("\nEnter Hire Date (mm/dd/yyyy): ")
        HireDt = datetime.strptime(HireDt_str, "%m/%d/%Y").date()
        crud.Insert_Into_Empl_Table(Fnm, Lnm, Gender, DOB, HireDt, conn)

    else:
        print("Wrong option chosen\n")

    print()
    crud.Select_Data_All(conn)

    conn.close()

    print("\nBye!")

if __name__ == "__main__":
    main()
