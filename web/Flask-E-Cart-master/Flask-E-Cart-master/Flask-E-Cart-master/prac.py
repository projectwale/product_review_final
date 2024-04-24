import pandas as pd
import pymysql

def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="pola")
        return connection
    except:
        print("Something went wrong in database Connection")


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")


con=dbConnection()
cursor=con.cursor()

# df = pd.read_csv("bk1.csv")

data = pd.read_csv (r'bk1.csv')   
df = pd.DataFrame(data)

# productId = list(df['productId'])
# name = list(df['name'])
# price = list(df['price'])
# image = list(df['image'])
# stock = list(df['stock'])
# categoryId = list(df['categoryId'])


for row in df.itertuples():    
    print(row)
    con = dbConnection()
    cursor = con.cursor()
    sql1 = "INSERT INTO product(productId,name,price,description,image,stock,categoryId) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]))
    cursor.execute(sql1,val1)
    con.commit()

# for row in df.itertuples():
#     cursor.execute("INSERT INTO product(productId,name,price,image,stock,categoryId) VALUES (%s,%s,%s,%s,%s,%s)", row.productId, row.name, row.price,row.image, row.stock, row.categoryId)
# con.commit()

