from flask import *
import sqlite3,hashlib, os
from werkzeug.utils import secure_filename
# from flask import Flask, render_template, request
import pickle
import pymysql
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import socket
from datetime import datetime

global col
global dt
global productData
global loggedIn
global firstName
global noOfItems

app = Flask(__name__)

def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="pola",charset='utf8')
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

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'random string'

##########################################################################################################
#                                           Register
##########################################################################################################
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #Parse form data    
        # print("hii register")
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
        username = request.form['username']
        add = request.form['add']
        postc = request.form['postc']
        mob = request.form['mob']
        productId = 0
        # print(password)
        # print(cpassword)
        # print(email)
        # print(username)
        # print(add)
        # print(postc)
        # print(mob)
        # print(productId)
        try: 
            con = dbConnection()
            cursor = con.cursor()
            sql1 = "INSERT INTO users (username, email, pass) VALUES (%s, %s, %s)"
            val1 = (username, email, password)
            cursor.execute(sql1, val1)
            print("query 1 submitted")
            sql2 = "INSERT INTO address (username, email, address, postcode, mobile) VALUES (%s, %s, %s, %s, %s)"
            val2 = (username, email, add, str(postc), str(mob))
            cursor.execute(sql2, val2)
            print("query 2 submitted")
            sql3 = "INSERT INTO kart1 (username, productId) VALUES (%s, %s)"
            val3 = (username, int(productId))
            cursor.execute(sql3, val3)
            print("query 3 submitted")
            con.commit()
        except:
            con.rollback()
            msg = "Error occured"
            return render_template("login.html", error=msg)
        finally:
            dbClose()
        return render_template("login.html")
    return render_template("register.html")
##########################################################################################################
#                                               Login
##########################################################################################################
@app.route("/", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'] 

        # print(email)
        # print(password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM users WHERE email = %s AND pass = %s', (email, password))
        result = cursor.fetchone()
        print("result")
        print(result)
        if result_count>0:
            print("len of result")
            session['uname'] = result[1]
            session['userid'] = result[0]
            return redirect(url_for('root'))
        else:
            return render_template('login.html')
    return render_template('login.html')
##########################################################################################################
#                                       Home page
##########################################################################################################
def getLoginDetails():
    loggedIn = True
    con = dbConnection()
    cursor = con.cursor()
    

    sql1 = ("SELECT id, username FROM users WHERE username = %s")
    val = (session['uname'])
    cursor.execute(sql1, val)
    
    userId= cursor.fetchone()
    
    sql2 = ("SELECT username,productId FROM kart1 WHERE username = %s")
    val2 = val
    cursor.execute(sql2, val2)

    noOfItems = cursor.fetchone()
    print("noOfItems")
    print(noOfItems[0])
    
    username = noOfItems[0]
    count_item = noOfItems[1]
    return loggedIn, username, count_item

@app.route("/root")
def root():
    if 'uname' in session:
        print(" hii root")
        loggedIn, username, count_item = getLoginDetails()
        con = dbConnection()
        cursor = con.cursor()
        # cursor.execute("SELECT productId, name, price, description, image, stock FROM product")
        # result1 = cursor.fetchone()
        # cursor.execute("SELECT categoryId, name FROM categories")
        # categoryData = cursor.fetchone()
        cursor.execute("SELECT productId, name, price, description, image, stock FROM product")
        result1 = cursor.fetchone()
        cursor.execute("SELECT categoryId, name FROM categories")
        categoryData = cursor.fetchone()
        con.commit()   

    return render_template('home.html', loggedIn=loggedIn, firstName=username, noOfItems=count_item, categoryData=categoryData)
##########################################################################################################
#                                       Product Description
##########################################################################################################
@app.route("/productDescription", methods = ['POST', 'GET'])
def productDescription():
    global col
    global dt
    global productData
    global loggedIn
    global firstName
    global noOfItems

    loggedIn, username, count_item = getLoginDetails()
    productId = request.args.get('productId')
    print("productId")
    print(productId)
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT productId, name, price, description, image, stock FROM product WHERE productId = ' + productId)
    productData = cursor.fetchone()
    print("productData")
    # print(productData[3][0])
    cursor.execute('SELECT categoryId FROM product WHERE productId = ' + productId)
    cat_dat = cursor.fetchone()
    con.close()
    # print("cat_dat")
    # print(cat_dat[0])
    df = pd.read_csv(str(cat_dat[0])+".csv")
    col = df.columns
    # print("df[col[0]]")
    a = str(df[col[0]])[5:]
    print(a)
    dt = [str(df[col[0]])[5:],str(df[col[1]])[5:],str(df[col[2]])[5:],str(df[col[3]])[5:],str(df[col[4]])[5:],str(df[col[5]])[5:],str(df[col[6]])[5:],str(df[col[7]])[5:],str(df[col[8]])[5:],str(df[col[9]])[5:],str(df[col[10]])[5:],str(df[col[11]])[5:],str(df[col[12]])[5:],str(df[col[13]])[5:],str(df[col[14]])[5:]]
    # print(dt)
    return render_template('item.html',colm=col, dt=dt, data=productData, loggedIn=loggedIn, firstName=username, noOfItems=count_item)
##########################################################################################################
#                                       Review part
##########################################################################################################
@app.route("/review", methods = ['POST', 'GET'])
def review():
    if 'uname' in session and request.method == 'POST':
        
        global col
        global dt
        global productData
        global loggedIn
        global firstName
        global noOfItems
        
        print(" hii root")
        ####################### Retrive login details #####################
        loggedIn, username, count_item = getLoginDetails()
        ####################### Predicting true or fake #####################
        df = pd.read_csv("processed.csv")
        loggedIn, username, count_item = getLoginDetails()

        Tfidf_vect = TfidfVectorizer(max_features=5000, sublinear_tf=True, decode_error='ignore')
        Tfidf_vect.fit(df['lemitized_review_text'])
        #Train_X_Tfidf = Tfidf_vect.transform(Train_X)
        # Test_X_Tfidf = Tfidf_vect.transform(Test_X)

        txt = request.form['addComment']
        tf2=Tfidf_vect.transform([txt])
        op=""
        with open(r'models/nb_pickle1','rb') as f:
            mp1=pickle.load(f)
            red1=mp1.predict(tf2)
        if red1==0:
            print("review is Positive predicted by Naive Bayes")
            a = "Positive"
            op=a
        elif red1==1:
            print("review is Negative predicted by Naive Bayes")
            b = "Negative"
            op = b
        else:
            print("Somthing went wrong detected by Naive Bayes")
        ####################### Fetching Ip adress and report count #####################
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)   
        print("Your Computer Name is:"+hostname)   
        print("Your Computer IP Address is:"+IPAddr)
        report_count="0"
        ####################### Fetching time and date #####################
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        print("date and time =", dt_string)
        
        dicts = {"username":username, 
                 "txt":txt, 
                 "IPAddr":IPAddr, 
                 "op":op, 
                 "dt_string":dt_string, 
                 "report_count":report_count}
        return dicts

if __name__=='__main__':
    app.run('0.0.0.0')