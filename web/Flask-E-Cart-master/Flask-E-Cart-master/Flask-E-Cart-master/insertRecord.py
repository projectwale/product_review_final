import pandas as pd
import pyodbc
import pymysql

# Import CSV
data = pd.read_csv (r'books.csv')   
df = pd.DataFrame(data)

def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="bookmaster")
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

# Insert DataFrame to Table
for row in df.itertuples():    
    con = dbConnection()
    cursor = con.cursor()
    sql1 = "INSERT INTO books (isbn, title, author, year) VALUES(%s,%s,%s,%s);"
    val1 = val1 = (row[1],row[2],row[3],row[4])
    cursor.execute(sql1,val1)
    con.commit()