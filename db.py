import sqlite3
from flask import request
# Connects to database
# The .db file is created automatically if it does not exist
con = sqlite3.connect('androidproject.db')

c=con.cursor()

# Creates table
c.execute("""CREATE TABLE IF NOT EXISTS USER (
    USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    USER_NAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL
    );""")

c.execute("""CREATE TABLE IF NOT EXISTS RECORD (
    RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    USER_ID INTEGER NOT NULL,
    DATE TEXT NOT NULL,
    TIME TEXT NOT NULL,
    NAME TEXT NOT NULL,
    GRAIN TEXT NOT NULL,
    MEAT TEXT NOT NULL,
    SEAFOOD TEXT NOT NULL,
    VEGETABLE TEXT NOT NULL,
    FRUIT TEXT NOT NULL,
    DAIRY TEXT NOT NULL
    );""")
c.execute('DELETE FROM USER;')
c.execute('DELETE FROM RECORD;')
user_list={
    (1,"A","password"),
    (2,"B","123"),
    (3,"C","aabBbcc")
}

    

# insert test data
#testData = ['Anthony', 'Ben', 'John', 'Kenneth', 'Loretta']
for user in user_list:
    insertQuery = "INSERT INTO USER values (?,?,?);"
    con.execute(insertQuery, user)
record_list={

    (1,2,"2023/11/23","12:25:30","burger","1","1","0","1","0","1"),
    (2,1,"2023/11/27","03:11:12","pizza1","1","1","0","0","0","1"),
    (3,1,"2023/11/28","04:37:11","pizza2","1","1","0","0","0","1"),
    (4,1,"2023/11/29","03:56:43","pizza3","1","1","0","0","0","1"),
    (5,1,"2023/11/30","02:21:56","pizza4","1","0","0","0","0","1"),
    (6,1,"2023/12/1","01:14:34","pizza5","1","1","0","0","0","1"),
    (8,1,"2023/12/2","00:25:14","pizza6","1","1","0","0","0","1"),
    (7,3,"2023/11/24","12:00:00","Steak","0","1","0","0","0","0"),

    (24,3,"2023/11/19","12:00:00","test","0","1","0","1","0","0"),
    (25,3,"2023/11/19","18:00:00","test","0","1","0","0","0","1"),
    (9,3,"2023/11/20","11:00:00","test","1","1","1","0","0","0"),
    (10,3,"2023/11/20","19:00:00","test","1","0","0","0","0","0"),
    (11,3,"2023/11/21","13:00:00","test","1","0","1","1","0","1"),
    (12,3,"2023/11/21","20:00:00","test","1","0","0","0","0","0"),
    (13,3,"2023/11/22","13:00:00","test","1","1","0","1","0","0"),
    (14,3,"2023/11/22","20:00:00","test","1","1","0","1","0","0"),
    (15,3,"2023/11/23","12:00:00","test","1","1","1","1","0","1"),
    (16,3,"2023/11/23","19:00:00","test","1","0","0","0","0","0"),
    (17,3,"2023/11/24","12:00:00","test","1","0","0","0","0","0"),
    (18,3,"2023/11/24","20:00:00","test","1","0","1","1","0","1"),
    (19,3,"2023/11/25","12:00:00","test","0","1","1","1","0","0"),
    (20,3,"2023/11/25","19:00:00","test","0","1","0","0","0","0"),

    (21,3,"2023/11/23","16:00:00","test","0","0","0","0","0","1"),
    (22,3,"2023/11/21","15:00:00","test","0","0","0","0","1","0"),
    (23,3,"2023/11/19","16:00:00","test","0","0","0","0","1","0"),
    (26,3,"2023/11/24","15:00:00","test","0","0","0","1","0","1"),

}


for record in record_list:
    insertQuery = "INSERT INTO RECORD values (?,?,?,?,?,?,?,?,?,?,?);"
    con.execute(insertQuery, record)

con.commit()
con.close()