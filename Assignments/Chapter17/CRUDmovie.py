import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
#----------------------------------------------
def DBConnection() :
    ##### Open the Word doc attached and do those things first.

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
#-----------------------------------------------
def Create_Table_Empl(conn) :
  
    TABLES = {}
    TABLES['Employees_Guha'] = (
        "CREATE TABLE `Employee_Guha` ("
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
#------------------------------------------
def Create_Table_Movie(conn) :
  
    TABLES = {}
    TABLES['Movie_Guha'] = (
        "CREATE TABLE `Movie_Guha` ("
        "  MovieID integer NOT NULL AUTO_INCREMENT,"
        "  CategoryID integer NULL,"
        "  Name varchar(50) NULL,"
        "  MakeYear integer NULL,"
        "  Minutes integer NULL,"
        "  RelzDate date NULL,"
        "  PRIMARY KEY (`MovieID`)"
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
#------------------------------------------
def Create_Table_Category(conn) :
  
    TABLES = {}
    TABLES['Category_Guha'] = (
        "CREATE TABLE `Category_Guha` ("
        "  `CategoryID` integer NOT NULL AUTO_INCREMENT,"      
        "  `Name' varchar(50) NOT NULL,"      
        "  PRIMARY KEY (`CategoryID`)"
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
#------------------------------------------
def Create_View_vuMovie(conn) :

    #DROP VIEW [IF EXISTS] [schema_name.]viewEmployee;
    try:
        query = """CREATE or REPLACE VIEW vuMovie_Guha as \
              SELECT MovieID, Name, MakeYear FROM  Movie_Guha"""

        crsr = conn.cursor()
        crsr.execute(query)
        result = crsr.fetchall()
        conn.commit()

    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("View Created/Re-Created!")            
#-----------------------------------------------
def Select_All_Data(conn) :

    query = "SELECT CONVERT(MovieID,char) as mvid, \
                    CONVERT(CategoryID,char) as catid, \
                    name, \
                    convert(makeYear,char) as mkyr, \
                    convert(minutes,char) as mnts,  \
                    date_format(relzDate, '%m-%d-%Y')  as rlzdt  \
              FROM  Movie_Guha " 

    crsr = conn.cursor()
    crsr.execute(query)
    result = crsr.fetchall()

    mvid = "MovieID"
    catid = "CatgID"
    nme = "Name"
    mkyr = "MakeYr"
    mnts = "Minutes"
    rlzdt = "RelzDate"
    
    if crsr.rowcount >= 1 :
       print(f"{mvid:<8}{catid:<8}{nme:<30}{mkyr:<10}{mnts:<10}{rlzdt:<10}")
    
    for r in result:
        rr = ",".join(r)
        rec = rr.split(',')

        mvid  = rec[0]
        catid = rec[1]
        nme   = rec[2]
        mkyr  = rec[3]
        mnts  = rec[4]
        rlzdt = rec[5]
        
        print(f"{mvid:<8}{catid:<8}{nme:<30}{mkyr:<10}{mnts:<10}{rlzdt:<10}")

    conn.commit()
    return crsr.rowcount 
#---------------------------------
def Select_From_vuMovie(conn) :

    query = "SELECT CONVERT(MovieID,char) as mvid, Name, \
             CONVERT(MakeYear,char) as mkyr \
             FROM  vuMovie_Guha " 

    crsr = conn.cursor()
    crsr.execute(query)
    result = crsr.fetchall()
  
    mvid = "MovieID"
    nme = "Name"
    mkyr = "MakeYr"
    print()
    print(f"{mvid:<10}{nme:<35}{mkyr:<11}")
    
    for r in result:
        r1 = ",".join(r)
        rec = r1.split(',')
        
        mvid = rec[0]
        nme = rec[1]       
        mkyr = rec[2]
        print(f"{mvid:<10}{nme:<35}{mkyr:<11}")
   
    if crsr.rowcount >= 1 :
       print("\nSelect from view is successful\n")
    else :
      print("\nSelect from view is not successful\n")

    conn.commit()
#------------------------------------
def Insert_Into_Movie_Table(inptVal, conn):

    #insert into sp2024python.movie_guha (categoryID, name, makeYear, minutes, relzdate)
    #values (1, 'Sholay', 1976, 180, '1987-03-22')
    
    ctid = 0  #initializing local vars
    nme  = 0
    mkyr = 0
    mnts = 0
    rlMM = 0
    rlDD = 0
    rlYY = 0
    
    Insert_stmt = ("INSERT INTO Movie_Guha "
                   "(categoryID, name, makeYear, minutes, relzdate) "
                   "VALUES (%s, %s, %s, %s, %s)")

    crsr = conn.cursor()

    rec = inptVal.split(',') 

    ctid = rec[0]
    nme  = rec[1] 
    mkyr = rec[2]   
    mnts = rec[3]
    rlzdt= rec[4]

    rl = rlzdt.split('/')
    rlMM = int(rl[0])
    rlDD = int(rl[1])
    rlYY = int(rl[2])  
    
    new_data = (ctid, nme, mkyr, mnts, date(rlYY, rlMM, rlDD))
    
    crsr.execute(Insert_stmt, new_data)
    
    if crsr.rowcount == 1 : 
       print("\nInsert is successful\n")
    else :
       print("\nInsert is not successful\n")
      
    conn.commit()
#---------------------------------
def Update_Movie_Table(mvid, updtVal, conn):

    rlzMM = 0
    rlzDD = 0
    rlzYY = 0
    
    crsr = conn.cursor()

    rec = updtVal.split(',')   
 
    catidNew = rec[0]
    nmeNew   = rec[1]
    mkyrNew  = rec[2]
    minNew   = rec[3]
    rlzdtNew = rec[4]

    rec = ""
    rtn = Select_Data_By_MovieId(mvid, conn)
    if rtn == 'n' :  # means rec couldn't be pulled successfully
       print("\nRec not pulled successfully!\n")
       exit()

    rec = rtn.split(',')
    
    catidOld = rec[0].strip()
    nmeOld   = rec[1].strip()
    mkyrOld  = rec[2].strip()
    minOld   = rec[3].strip()
    rlzdtOld = rec[4].strip()

    if catidNew == "" :
       catidNew = catidOld
       
    if nmeNew == "" :
       nmeNew = nmeOld 
       
    if mkyrNew == "" :
       mkyrNew = mkyrOld

    if minNew == "" :
       minNew = minOld

    if rlzdtNew == "" :
       rlzdtNew = rlzdtOld
    rlzdtNew = rlzdtNew.replace("/","-")
    
    rlz = rlzdtNew.split('-')
    rlzMM = int(rlz[0])
    rlzDD = int(rlz[1])
    rlzYY = int(rlz[2])  
    
    new_data = (catidNew, nmeNew, mkyrNew, minNew, date(rlzYY, rlzMM, rlzDD), mvid)
    
    Update_stmt = ("UPDATE Movie_Guha   \
                    SET categoryID = %s, \
                    name = %s, \
                    makeYear = %s,      \
                    minutes = %s,   \
                    relzDate = %s   \
                    WHERE movieID  = %s" )
    
    crsr.execute(Update_stmt, new_data)
    
    if crsr.rowcount == 1 :
       print("\nUpdate is successful\n")
    else :
       print("\nUpdate is not successful\n")
       
    conn.commit()  
#-----------------------------------------------
def Select_Data_By_MovieId(mvid,conn) :

    query = "SELECT CONVERT(CategoryID,char) as catid, \
                    name, \
                    convert(makeYear,char) as mkyr, \
                    convert(minutes,char) as mnts,  \
                    date_format(relzDate, '%m-%d-%Y')  as relzDt  \
               FROM  Movie_Guha where MovieId = " + mvid 

    crsr = conn.cursor()
    crsr.execute(query)
    result = crsr.fetchall()

    if result == "" :
       print("\nRec not found\n")
       rtn = 'n'
    else :
        for r in result:
            rr = ",".join(r)
            rec = rr.split(',')

            catid = rec[0]
            nme = rec[1]
            mkyr = rec[2]
            mnts = rec[3]
            rlzdt = rec[4]
        
        if crsr.rowcount >= 1 :         
           #print("\nSelect is successful\n")
           rtn = rr
        else :
           #print("\nSelect is not successful\n")
           rtn = 'n'

    conn.commit() 
    return rtn
#------------------------------------------
def Delete_Movie_Table(mvid, conn):
 
    crsr = conn.cursor()
    
    Delete_stmt = ("DELETE From Movie_Guha WHERE movieID = %s" )
 
    actual_data = (mvid,)   # remember comma at the end
   
    crsr.execute(Delete_stmt, actual_data)
    
    if crsr.rowcount == 1 :
       print("\nDelete is successful\n")
    else :
      print("\nDelete is not successful\n")
      
    conn.commit()
#-----------------------------------------------  
#print("Bye")
