

###  DISCLAMER ###

#this code can be better, we can create a abstract class to represent an database

#Maybe Jadson and kamila can do

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "filial "
)

mycursor = mydb.cursor()


#the %s turn the code more secure and prevent sql injection

def insert(tbl_name,fieldname1, fieldname2, fieldname3, value1, value2,value3):
    sql = "INSERT INTO {} ({}, {}, {}) VALUES(%s %s %s).".format(tbl_name,fieldname1, fieldname2, fieldname3)
    values = (value1, value2,value3)
    mycursor.execute(sql, values)


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






