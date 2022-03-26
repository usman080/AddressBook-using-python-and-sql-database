#Python Project: Address Book
#Author: Mr. Patel Usman
#Date: 25/09/2020
#Roll NO: B-47

import sqlite3
from sqlite3 import Error
import datetime

def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print("Database Opening Error")
    return conn

def insert(conn):
    ID = int(input("Enter Id:"))
    Firstname = input("Enter Your Firstname:")
    Middlename = input("Enter your Middlename:")
    Lastname = input("Enter your Lastname:")
    birth_year = int(input("Enter birth year:"))
    birth_month = int(input("Enter birth month:"))
    birth_date = int(input("Enter birth date:"))
    HouseNo = input("Enter house No.:")
    LaneNO = input("Enter  Lane No.")
    LandMark = input("Enter Land Mark:")
    Address = input("Enter Address(Area):")
    City = input("Enter City:")
    District = input("Enter District:")
    State = input("Enter State:")
    Pincode = input("Enter Pincode:")
    MobileNo = input("Enter Mobile No:")
    Email = input("Enter Email Id:")
    DOB = datetime.date(birth_year,birth_month,birth_date)
    sql = '''insert into AddressBook(ID,Firstname, Middlename,Lastname,DOB,HouseNo, LaneNO ,LandMark, Address, City,District, State, Pincode, MobileNo ,Email) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    data = (ID,Firstname, Middlename,Lastname,DOB,HouseNo, LaneNO ,LandMark, Address, City,District, State, Pincode, MobileNo ,Email,)
    cur.execute(sql, data)
    conn.commit()
    print("Data Inserted Sucessfully!")
    return cur.lastrowid
def search(conn):
    cur = conn.cursor()
    print("*******MENU********")
    print("1.Search By ID")
    print("2.Search By DOB")
    ch = int(input("Enter your choice for Search:"))
    if(ch==1):
        ID = int(input("Enter ID:"))
        cur.execute("Select * from AddressBook where ID= ?",(ID,))
        print("ID|Firstname|Middlename|Lastname|DOB|HouseNo|LaneNO|LandMark|Address|City|District|State|Pincode|MobileNo|Email")
        rows = cur.fetchall()
        for i in rows:
            print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|",i[8],"|",i[9],"|",i[10],"|",i[11],"|",i[12],"|",i[13],"|",i[14])
    elif(ch==2):
        birth_year = int(input("Enter birth year:"))
        birth_month = int(input("Enter birth month:"))
        birth_date = int(input("Enter birth date:"))
        DOB = datetime.date(birth_year, birth_month, birth_date)
        cur.execute("Select * from AddressBook where DOB= ?",(DOB,))
        print("ID|Firstname|Middlename|Lastname|DOB|HouseNo|LaneNO|LandMark|Address|City|District|State|Pincode|MobileNo|Email")
        rows = cur.fetchall()
        for i in rows:
            print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|",i[8],"|",i[9],"|",i[10],"|",i[11],"|",i[12],"|",i[13],"|",i[14])

def update(conn):
    print("*******MENU********")
    print("1.Name/Birthdate")
    print("2.Address")
    print("3.Mobile No / Email")
    ch = int(input("Enter your choice for update"))
    cur = conn.cursor()
    if(ch==1):
        ID = int(input("Enter ID"))
        Firstname = input("Enter New Firstname:")
        Middlename = input("Enter New Middlename:")
        Lastname = input("Enter New Lastname:")
        birth_year = int(input("Enter new birth_year:"))
        birth_month = int(input("Enter new birth_month:"))
        birth_date = int(input("Enter new birth_date:"))
        DOB = datetime.date(birth_year,birth_month,birth_date)
        data = (Firstname, Middlename,Lastname,DOB,ID)
        sql = '''update AddressBook set Firstname=?, Middlename=?, Lastname=?, DOB=? where ID=?  ''' 
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        print("Data updated Sucessfully!")
        return cur.lastrowid
    elif(ch==2):
        ID = int(input("Enter ID:"))
        HouseNo = input("Enter house No.:")
        LaneNO = input("Enter  Lane No.")
        LandMark = input("Enter Land Mark:")
        Address = input("Enter Address(Area):")
        City = input("Enter City:")
        District = input("Enter District:")
        State = input("Enter State:")
        Pincode = input("Enter Pincode:")
        data=(HouseNo, LaneNO ,LandMark, Address, City,District, State, Pincode,ID)
        sql = '''update AddressBook set HouseNo=?, LaneNo=?, LandMark=?, Address=?, City=?, District=?, State=?, Pincode=? where ID=?'''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Data updated successfully!")
        return cur.lastrowid
    elif(ch==3):
        ID = int(input("Enter ID:"))
        MobileNo = input("Enter New Mobile No:")
        Email = input("Enter New Email Id:")
        data = (MobileNo ,Email,ID)
        sql = '''update AddressBook set MobileNo=? ,Email=? where ID=?'''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Data updated successfully!")
        return cur.lastrowid

def delete(conn):
    ID = int(input("Enter ID:"))
    sql = 'delete from AddressBook where ID=?'
    cur = conn.cursor()
    cur.execute(sql,(ID,))
    print("Data Deleted Sucessfully!")
    conn.commit()
    
def main():
    try:
        database = r"C:\Users\Addl.DIO\Desktop\AddressBook\AddressBook.db"
        conn = connection(database)
        with conn:
            print("**********************************************************************************AddressBook************************************************************************")
            print("*******MENU********")
            print("1. Insert AddressBook")
            print("2. Search AddressBook")
            print("3. Update AddressBook")
            print("4. Delete AddressBook")
            ch = int(input("Enter your Choice (1-4) : "))
            if(ch == 1):
                id = insert(conn)
            elif(ch == 2):
                id = search(conn)
            elif(ch==3):
                id = update(conn)
            elif(ch ==4):
                id = delete(conn)
    except Error as e:
        print("Error in Database Connection", e)
if __name__ =="__main__":
    main()
