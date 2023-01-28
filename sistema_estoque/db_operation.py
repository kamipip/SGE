



import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "filial "
)

mycursor = mydb.cursor()




def insert(tbl_name,fieldname1, fieldname2, fieldname3, value1, value2,value3):
    #sql = "INSERT INTO informacoes_filial (nome, tipo, endereco) VALUES (%s, %s, %s)"

    sql = "INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(tbl_name, fieldname1, fieldname2, fieldname3)
   
    values =  (value1, value2, value3)
    
    mycursor.execute(sql, values)

    mydb.commit()

    print("Record")



def update(tbl_name, field,old_value, new_value):
    #Little Trick to inject transform old_values in new_values

    sql = "UPDATE {} SET {} = %s WHERE address = %s".format(tbl_name, field)
    values = (old_value, new_value)
    mycursor.execute(sql,values)
    mydb.commit()

def delete(tbl_name, field, value):
    sql = "DELETE FROM {} WHERE {} = '{}'".format(tbl_name, field, value)
    mycursor.execute(sql)
    mydb.commit()






