
import sys
sys.path.insert(0,'C:/Users/taiea/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/Scripts')
import flask
import sqlite3
import io
import os
import base64
from flask import request,send_file
app = flask.Flask(__name__)
@app.route('/getrecord', methods=['GET'])
def getrecord():
    #DONE
    user_id = request.args.get('user_id', '')
    con = sqlite3.connect('androidproject.db')
    #if len(name) > 0:
        # insert into db
     #   insertQuery = "INSERT INTO STUDENT (NAME) values (?);"
    #    con.execute(insertQuery, (name,))
    #    con.commit()
    # select from db
    records = []
    if len(user_id) > 0:
        #cursor = con.execute("SELECT * from RECORD WHERE USER_ID IN (SELECT USER_ID from USER WHERE USER_NAME=(?));",user_name)
        cursor = con.execute("SELECT * from RECORD WHERE USER_ID=(?);",user_id)
        for row in cursor:
            row_change={
                "date":row[2],
                "time":row[3],
                "name":row[4],
                "category":[row[5],row[6],row[7],row[8],row[9],row[10]],
                "record_id":row[0]
            }
            records.append(row_change)
    con.close()
    outdata = {
        "records": records
    }
    return outdata

@app.route('/newrecord', methods=['POST'])
def newrecord():
    #TO BE DONE
    record = request.json
    con = sqlite3.connect('androidproject.db')
    if len(record) > 0:
        # insert into db
        insertQuery = "INSERT INTO RECORD values (null,?,?,?,?,?,?,?,?,?,?);"
        con.execute(insertQuery, (record["user_id"],record["date"],record["time"],records["category"][0],records["category"][1],records["category"][2],records["category"][3],records["category"][4]))
        con.commit()
    con.close()
    outdata = {
        "message": "success"
    }
    return outdata
    
@app.route('/login', methods=['GET'])
def login():
    #DONE
    print("login")
    user_name = request.args.get('user_name', '')
    password = request.args.get('password', '')
    con = sqlite3.connect('androidproject.db')
    outdata = {
        "success": False,
        "user_id": -1,
        "records": []
    }
    print(user_name)
    print(password)
    if len(user_name) > 0 and len(password) > 0:
        print("not null")
        records = []
        #cursor = con.execute("SELECT * from RECORD WHERE USER_ID IN (SELECT USER_ID from USER WHERE USER_NAME=(?));",user_name)
        cursor = con.execute("SELECT * from USER WHERE USER_NAME=(?);",user_name)
        for row in cursor: 
            #print(row[2])
            if password==row[2]: #row[2] is the password stored in database
                print("correct")
        
                outdata["success"]=True
                outdata["user_id"]=row[0]

        print(outdata["user_id"])
        if outdata["user_id"]!=-1:
            cursor = con.execute("SELECT * from RECORD WHERE USER_ID=(?);",str(outdata["user_id"]))
            for row in cursor:
                row_change={
                    "date":row[2],
                    "time":row[3],
                    "name":row[4],
                    "category":[row[5],row[6],row[7],row[8],row[9],row[10]],
                    "record_id":row[0]
                }
                records.append(row_change)
            outdata["records"]=records
    
    con.close()
    return outdata
    print()



@app.route('/uploadrecord', methods=['POST'])
def uploadimage():
    #DONE

    
    user_id=int(request.values["user_id"])
    name=request.values["name"]
    date=request.values["date"]
    time=request.values["time"]
    Grain=request.values["Grain"]
    Meat=request.values["Meat"]
    Seafood=request.values["Seafood"]
    Vegetable=request.values["Vegetable"]
    Fruit=request.values["Fruit"]
    Dairy=request.values["Dairy"]
    image=request.values["IMG"]
    if user_id !=-1:
        # insert into db
        con = sqlite3.connect('androidproject.db')
        insertQuery = "INSERT INTO RECORD values (null,?,?,?,?,?,?,?,?,?,?);"
        con.execute(insertQuery, (user_id,date,time,name,Grain,Meat,Seafood,Vegetable,Fruit,Dairy))
        con.commit()

        cursor = con.execute("SELECT * from RECORD WHERE USER_ID=(?) AND DATE=(?) AND TIME=(?);",(user_id,date,time))
        record_id=""
        for row in cursor:
            record_id=row[0]
            print(record_id)
    
        if image!="":
            print("r:",image)
            image = base64.b64decode(image)
            with open(os.getcwd()+"/image/"+str(record_id)+".jpg", 'wb') as f:
                f.write(image)

    
    return "success"
        
 

@app.route('/requestimage', methods=['GET'])
def requestimage():
    #DONE
    record_id = request.args.get('record_id', '')
    print(record_id)


    
    try:
        with open(os.getcwd()+"/image/"+record_id+".jpg", 'rb') as bites:
            print("get image")
            return send_file(
                io.BytesIO(bites.read()),
                mimetype='image/.jpg'
            )
    except IOError:
        return ""
    print()
# adds host="0.0.0.0" to make the server publicly available
app.run(host="0.0.0.0")