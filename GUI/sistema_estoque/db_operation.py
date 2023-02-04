import mysql.connector



#Adding try to connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "produto"
)



mycursor = mydb.cursor()








def insert(tbl_name,fieldname1, fieldname2, fieldname3,fieldname4,value1, value2,value3,value4):
    #sql = "INSERT INTO informacoes_filial (nome, tipo, endereco) VALUES (%s, %s, %s)"

    sql = "INSERT INTO {} ({}, {}, {}, {}) VALUES (%s, %s, %s, %s)".format(tbl_name, fieldname1, fieldname2, fieldname3, fieldname4)
   
    values =  (value1, value2, value3, value4)
    


    #Command to commit in database it must be include in an try-catch

    try:
        mycursor.execute(sql, values)

        mydb.commit()

        print("Record Save")
        print(mydb.commit())

     #Rewrite to support personal mysql or mariadb erros   
    except mysql.connector.Error as err:
        print(err)

def read_table():


    saida = mycursor.execute("SELECT * FROM informacoes_produto")

    myresult = mycursor.fetchall()

    mydb.commit()

    print(myresult)

    return myresult





def update(tbl_name, field, old_value, new_value):
    #Little Trick to inject transform old_values in new_values

    sql = "UPDATE {} SET {} = '{}' WHERE {} = '{}' ".format(tbl_name, field, new_value, field, old_value)
    print(sql)


    try:
        mycursor.execute(sql)

        mydb.commit()

        print("Record Update")
     
    except mysql.connector.Error as err:
        print(err)
        print("Connection error")

def delete(tbl_name, field, value):
    sql = "DELETE FROM {} WHERE {} = '{}'".format(tbl_name, field, value)

    try:
        mycursor.execute(sql)

        mydb.commit()

        print("Record Delete")
     
    except mysql.connector.Error as err:
        print("Connection error")














