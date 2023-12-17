import mysql.connector as mysql

def getusername(id):
    mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT `firstname`, `lastname` FROM `member` WHERE id='{id}';")
    myresult = mycursor.fetchall()
    name = myresult[0][0] + " " + myresult[0][1]
    mycursor.close()
    mydb.close()
    return(str(name))

def getphone(id):
    mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT `phone` FROM `member` WHERE id='{id}';")
    myresult = mycursor.fetchall()
    phone = myresult[0][0]
    mycursor.close()
    mydb.close()
    return(str(phone))

def updatedb(id):
    mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM member WHERE id={id}")
    myresult = mycursor.fetchall()
    name = myresult[0][1] + " " + myresult[0][2]
    mycursor.execute(f"SELECT MAX(id) FROM rec{id}")
    a = mycursor.fetchall()[0][0]
    if a == None:
        result = f"{id}_8"
    else:
        result = f"{id}_" + str(a + 1)
    mycursor.execute(f"INSERT INTO rec{id} (name, par_state) VALUES (%s, %s)", (name, "normal"))
    print(result)
    mycursor.execute(f"""CREATE TABLE `{result}` (
        `data` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
        `predict_value` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
    mydb.commit()
    mycursor.close()
    mydb.close()

def insertdb(id, data, predict):
    mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb")
    # array_string = ','.join(data)
    array_string = ','.join(map(str, data))
    print(array_string, predict)
    
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT MAX(id) FROM rec{id}")
    table = f"{id}_" + str(mycursor.fetchall()[0][0])
    
    mycursor.execute(f"INSERT INTO {table} (data, predict_value) VALUES (%s, %s)", (array_string, predict))
    mydb.commit()
    mycursor.close()
    mydb.close()

def updatestate(id, state):
    mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT MAX(id) FROM rec{id}")
    myresult = mycursor.fetchall()[0][0]
    mycursor.execute(f"UPDATE rec{id} SET par_state = '{state}' WHERE id = '{myresult}'")
    mydb.commit()
    mycursor.close()
    mydb.close()