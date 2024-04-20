#!/usr/bin/env/python3

import CRUDmovie as crud
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
#-----------------------------------------------
def main() :
    conn = crud.DBConnection()
    
    crud.Create_Table_Movie(conn)
    crud.Create_View_vuMovie(conn)    
    
    print("Current Listing\n") 
    
    rtn = crud.Select_All_Data(conn)

    if rtn == 0 :  # means successful listing of recs
       input("\nFill table first by inserting rec : ")
       option = 'I'
    else :    
       option = input("\nEnter option (I/U/D/V) : ")
    
    if option.upper() == "U" :
       inpMvid =  input("\nEnter MovieId : ")
       inpCatid = input("\nEnter CatgId to update : ")
       inpName =  input("\nEnter Name   to update : ")
       inpMkyr =  input("\nEnter MakeYr to update : ")
       inpMin =   input("\nEnter Min    to update : ")
       inpRlzdt = input("\nEnter RlzDt  to update : ")
       
       if (inpMvid == "") :
           print("MovieId can't be blank\n")
       else :
           inpMvid = inpMvid.strip()
           updtVal = ""
           updtVal = inpCatid.strip() + ',' + inpName.strip() + ',' +  \
                     inpMkyr.strip() + ',' + inpMin.strip() + ',' + inpRlzdt.strip()
           
           crud.Update_Movie_Table(inpMvid, updtVal, conn)
       
    elif option.upper() == "D" :
         inpEmp = input("\nEnter EmpNo : ") 
         crud.Delete_Movie_Table(inpEmp, conn)
         
    elif option.upper() == "V" :      
         crud.Select_From_vuMovie(conn)

    elif option.upper() == "I" :
         inpCatid = input("\nEnter CategoryID   : ")
         inpNme   = input("\nEnter Name         : ")
         inpMkyr  = input("\nEnter MakeYr       : ")
         inpMin   = input("\nEnter Minutes      : ")
         inpRlzDt = input("\nEnter RelzDt(m/d/y): ")
 
         inptVal = ""
         inptVal = inpCatid.strip() + ',' + inpNme.strip() + ',' +  \
                   inpMkyr.strip() + ',' + inpMin.strip() + ',' + inpRlzDt.strip()
         
         crud.Insert_Into_Movie_Table(inptVal, conn)

    else :
         print("Wrong option chosen\n")

    print()
    crud.Select_All_Data(conn)  #re-displying
    
    crsr = conn.cursor()
    crsr.close()
    conn.close()
    
    print("\nBye!")       

if __name__ == "__main__":
    main()




