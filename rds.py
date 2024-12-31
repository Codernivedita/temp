#*********************************************************************************************************************
#Author - Nirmallya Mukherjee
#This script connects to a MySQL DB using multiple driver options
#*********************************************************************************************************************
import pymysql
import mysql.connector

hostname = 'flipbasket.c5tmm5lepe1g.us-east-1.rds.amazonaws.com'
username = 'root'
password = 'nivedita'
database = 'employees'

# Simple routine to run a query on a database and print the results:
def doQuery(conn) :
    cur = conn.cursor()
    cur.execute("SELECT emp_no, birth_date, first_name, last_name, gender FROM employees limit 10")
    for emp_no, birth_date, first_name, last_name, gender in cur.fetchall() :
        print (f"Emp No: {emp_no}, Birth Date: {birth_date}, First Name: {first_name}, Last Name: {last_name}, Gender: {gender}")


def pymysqlConnector() :
    print("Using pymysql")
    print("-------------")
    myConnection = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
    doQuery(myConnection)
    myConnection.close()


def mysqlConnector() :
    print("\n\nUsing mysql.connector")
    print("---------------------")
    myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    doQuery(myConnection)
    myConnection.close()


def createOrder() :
    print("\n\nUsing any of the above connectors, insert a new record in the orders table")
    conn = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    cur = conn.cursor()
    # TBD:You have to write this code and submit as part of the lab
    cur.execute("""
    INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date)
    VALUES ('1994-12-30', 'Nivedita', 'R', 'F', '2021-12-30')
""")

    conn.commit()
    cur.close()
    conn.close()


def main() :
    pymysqlConnector()
    mysqlConnector()
    createOrder()


main()

