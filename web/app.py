from dataclasses import replace
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

app = Flask(__name__)

global prdt_name
global prdt_price
global productData1
# global loggedIn
# global firstName
# global noOfItems
global prdt_img

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
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        add = request.form['add']
        postc = request.form['postc']
        mob = request.form['mob']
        productId = 0
        print(password)
        print(email)
        print(username)
        print(add)
        print(postc)
        print(mob)
        print(productId)
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
    return render_template("login.html")
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
#                                       Product Description
##########################################################################################################
@app.route("/single", methods = ['POST', 'GET'])
def productDescription():
    global prdt_name
    global prdt_price
    global productData1
    global loggedIn
    global firstName
    global noOfItems
    global prdt_img

    username=session.get('uname')
    productId = request.args.get('productId')
    
    # print("######### productId ####")
    # print(productId)
    con = dbConnection()
    cursor = con.cursor()

    cursor.execute('SELECT uname, comments FROM user_analysis where product_id = %s',(productId))
    cmnt = cursor.fetchall()
    print("### cmnt ####")
    print(cmnt)
    ################### fetching comments and username from database #############################
    unm=[]
    cm=[]
    for i in cmnt:
        a = i[0]
        unm.append(a)
        b = i[1]
        cm.append(b)
        # print("### a,b ####")
        # print(a,b)
        # break
    cmt = zip(unm,cm)  

    cursor.execute('SELECT name, price, description, image FROM product WHERE productId = ' + productId)
    productData = cursor.fetchone()
    productData = list(productData)
    # print("#### productData #####")
    # print(productData)

    prdt_name = productData[0]
    prdt_price = productData[1]
    prdt_disc = productData[2].split(',')
    productData1 = []
    for i in prdt_disc:
        prdt_disc1 = i.replace("\r\n","")
        productData1.append(prdt_disc1)
    print("#### prdt_disc #####")
    print(productData1)
    prdt_img = productData[3]


    cursor.execute('SELECT categoryId FROM product WHERE productId = ' + productId)
    cat_dat = cursor.fetchone()
    con.close()
    return render_template('single.html',cmt=cmt,  firstName=username, prdt_name=prdt_name, prdt_price=prdt_price,productId=productId, productData1=productData1, prdt_img=prdt_img )
##########################################################################################################
#                                               about
##########################################################################################################
@app.route("/about", methods = ['POST', 'GET'])
def about():
    username=session.get('uname')
    return render_template('about.html',firstName=username)
##########################################################################################################
#                                               Report
##########################################################################################################
@app.route("/report", methods = ['POST', 'GET'])
def report():
    username=session.get('uname')
    prd_name = request.args.get('prd_name')
    prd_name=list(prd_name.split('?'))
    prd_nm=prd_name[0]
    cmnt=prd_name[1]
    rprt=prd_name[2]

    # print("#### prd_name,cmnt,rprt ####")
    # print(prd_nm)
    # print(cmnt)
    # print(rprt)
    con = dbConnection()
    cursor = con.cursor()
    res_cont = cursor.execute('SELECT report FROM user_analysis WHERE product_name = %s and comments = %s', (prd_nm,cmnt))
    reprt = cursor.fetchone()
    # con.close()
    print("## reprt #")
    print(int(reprt[0]))
    report_num=int(reprt[0])
    report_num= report_num + 1

    sql1 = "UPDATE user_analysis SET report=%s WHERE product_name = %s and uname = %s"
    val1 = (str(report_num),prd_nm,username)
    cursor.execute(sql1, val1)
    con.commit()
    return redirect(url_for('root'))



    # return render_template('single.html',  firstName=username, prdt_name=prdt_name, prdt_price=prdt_price, productData1=productData1, prdt_img=prdt_img )
##########################################################################################################
#                                               contact
##########################################################################################################
@app.route("/contact", methods = ['POST', 'GET'])
def contact():
    username=session.get('uname')
    return render_template('contact.html',firstName=username)

##########################################################################################################
#                                               contact
##########################################################################################################
@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    # username=session.get('uname')
    session.pop('uname',None)
    return redirect(url_for('login'))
##########################################################################################################
#                                               Single page
##########################################################################################################
@app.route("/kart", methods = ['POST', 'GET'])
def kart():
    global prdt_name
    global prdt_price
    global productData1
    global loggedIn
    global firstName
    global noOfItems
    global prdt_img

    if request.method == 'POST':
        productId = request.form['productId']
        itm_name = request.form['item_name']
        amnt = request.form['amount']
        print("#### itm_name,amnt ########")
        print(productId,itm_name,amnt)

        username=session.get('uname')
        print(username)

        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute("SELECT name, price, description, image from product where name=%s", (itm_name))
        result = cursor.fetchone()
        result = list(result)
        print(result)
        print()

        prd_name = result[0]
        Price = result[1]
        description = result[2]
        img = result[3]

        uname = session.get("uname")
        result_count = cursor.execute("SELECT email, address, postcode, mobile from address where username=%s", (uname))
        result2 = cursor.fetchone()
        result2 = list(result2)
        email = result2[0]
        address = result2[1]
        postcode = result2[2]
        mobile = result2[3]

        # cursor.execute('SELECT name, price, description, image FROM product WHERE productId = ' + productId)
        # productData = cursor.fetchone()
        # productData = list(productData)
        # print("#### productData #####")
        # print(productData)

        # prdt_name = productData[0]
        # prdt_price = productData[1]
        # prdt_disc = productData[2].split(',')
        # productData1 = []
        # for i in prdt_disc:
        #     prdt_disc1 = i.replace("\r\n","")
        #     productData1.append(prdt_disc1)
        # print("#### prdt_disc #####")
        # print(productData1)
        # prdt_img = productData[3]

        print()
        print(result2)

        sql1 = "INSERT INTO kart1 (username, email, address,postcode,mobile,prd_name,Price,description,img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val1 = (uname, email, address,postcode,mobile,prd_name,Price,description,img)
        cursor.execute(sql1, val1)
        con.commit()
        print("query submitted")

        return render_template('kart.html',  firstName=username,description=description,Price=Price,prd_name=prd_name,img=img)
    return render_template('single.html')

##########################################################################################################
#                                       Home page
##########################################################################################################
@app.route("/root")
def root():
    if 'uname' in session:
        print(" hii root")
        username=session.get('uname')
        con = dbConnection()
        cursor = con.cursor()
        # username = session.get("user")

        # cursor.execute("SELECT productId, name, price, description, image, stock FROM product")
        # result1 = cursor.fetchone()
        # cursor.execute("SELECT categoryId, name FROM categories")
        # categoryData = cursor.fetchone()
        cursor.execute("SELECT productId, name, price, description, image, stock FROM product")
        result1 = cursor.fetchone()
        cursor.execute("SELECT categoryId, name FROM categories")
        categoryData = cursor.fetchone()
        con.commit()   

    return render_template('index.html',  firstName=username, categoryData=categoryData)

##########################################################################################################
#                                       Home page
##########################################################################################################
@app.route("/ordered", methods=["GET","POST"])
def ordered():
    if 'uname' in session and request.method=="POST":
        print(" hii root")
        username=session.get('uname')
        con = dbConnection()
        cursor = con.cursor()
        # username = session.get("user")

        # cursor.execute("SELECT productId, name, price, description, image, stock FROM product")
        # result1 = cursor.fetchone()
        # cursor.execute("SELECT categoryId, name FROM categories")
        # categoryData = cursor.fetchone()
        cursor.execute("SELECT productId, name, price, description, image, stock FROM product")
        result1 = cursor.fetchone()
        cursor.execute("SELECT categoryId, name FROM categories")
        categoryData = cursor.fetchone()
        con.commit()   

        flash("Your order has been placed! Thank you for shopping!","order")

    return render_template('index.html',  firstName=username, categoryData=categoryData)
##########################################################################################################
#                                       Review part
##########################################################################################################
@app.route("/review", methods = ['POST', 'GET'])
def review():
    if 'uname' in session and request.method == 'POST':
        print(" hii root")
        global prdt_name
        global prdt_price
        global productData1

        username=session.get('uname')
        txt = request.form['Message']
        prduct_nm = request.form['prduct_nm']
        ####################### Predicting true or fake #####################
        df = pd.read_csv("processed.csv")

        Tfidf_vect = TfidfVectorizer(max_features=5000, sublinear_tf=True, decode_error='ignore')
        Tfidf_vect.fit(df['lemitized_review_text'])
        #Train_X_Tfidf = Tfidf_vect.transform(Train_X)
        # Test_X_Tfidf = Tfidf_vect.transform(Test_X)

        

        tf2=Tfidf_vect.transform([txt])
        nbop=""
        with open(r'models/nb_pickle1','rb') as f:
            mp1=pickle.load(f)
            red1=mp1.predict(tf2)
        if red1==0:
            print("review is real predicted by Naive Bayes")
            a = "Real"
            nbop+=a
        elif red1==1:
            print("review is fake predicted by Naive Bayes")
            b = "Fake"
            nbop += b
        else:
            print("Somthing went wrong detected by Naive Bayes")

        svmop=""
        with open(r'models/svm_pickle1','rb') as f:
            mp1=pickle.load(f)
            red1=mp1.predict(tf2)
        if red1==0:
            print("review is real predicted by SVM")
            a = "Real"
            svmop+=a
        elif red1==1:
            print("review is fake predicted by SVM")
            b = "Fake"
            svmop += b
        else:
            print("Somthing went wrong detected by SVM")

        rfcop=""
        with open(r'models/rfc_pickle1','rb') as f:
            mp1=pickle.load(f)
            red1=mp1.predict(tf2)
        if red1==0:
            print("review is real predicted by Random Forest")
            a = "Real"
            rfcop+=a
        elif red1==1:
            print("review is fake predicted by Random Forest")
            b = "Fake"
            rfcop += b
        else:
            print("Somthing went wrong detected by Random Forest")
        ####################### Fetching Ip adress and report count #####################
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)   
        # print("Your Computer Name is:"+hostname)   
        # print("Your Computer IP Address is:"+IPAddr)
        ####################### Buy or not #####################
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT username FROM kart1 WHERE username = %s and prd_name = %s', (username,prduct_nm))
        res = cursor.fetchone()
        # print("result")
        # print(res)
        if result_count==0:
            buy_not="0"
        else:
            buy_not="1"
        rep_count="0"
        ####################### Prodct name #####################
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT productId FROM product WHERE name = %s', (prduct_nm))
        prdt_id = cursor.fetchone()
        print("## Prodct name ###")
        print(list(prdt_id)[0])

        cursor.execute('SELECT name, price, description, image FROM product WHERE productId = ' + list(prdt_id)[0])
        productData = cursor.fetchone()
        productData = list(productData)
        # print("#### productData #####")
        # print(productData)

        prdt_name = productData[0]
        prdt_price = productData[1]
        prdt_disc = productData[2].split(',')
        productData1 = []
        for i in prdt_disc:
            prdt_disc1 = i.replace("\r\n","")
            productData1.append(prdt_disc1)
        print("#### prdt_disc #####")
        print(productData1)
        prdt_img = productData[3]

        ####################### Fetching time and date #####################
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        # print("date and time =", dt_string)

        con = dbConnection()
        cursor = con.cursor()

        sql2 = "INSERT INTO user_analysis (product_id,product_name, uname, comments, ipadd, nb_real_fake, svm_real_fake, rf_real_fake, time_stmp, buy1_not0,report) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val2 = (prdt_id,str(prduct_nm), str(username), str(txt), str(IPAddr), str(nbop), str(svmop), str(rfcop), str(dt_string), str(buy_not),str(rep_count))
        cursor.execute(sql2, val2)
        con.commit()   
        print("All data feed to database")

    return render_template('single.html',  firstName=username, txt=txt, prdt_name=prduct_nm, prdt_price=prdt_price, productData1=productData1, prdt_img=prdt_img )

##########################################################################################################
#                                      Admin part
##########################################################################################################
@app.route("/adregister", methods = ['GET', 'POST'])
def adregister():
    if request.method == 'POST':
        #Parse form data    
        # print("hii register")
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        print(password)
        print(email)
        print(username)
        try: 
            con = dbConnection()
            cursor = con.cursor()
            sql1 = "INSERT INTO admin (username, email, pass) VALUES (%s, %s, %s)"
            val1 = (username, email, password)
            cursor.execute(sql1, val1)
            print("query 1 submitted")
            con.commit()
        except:
            con.rollback()
            msg = "Error occured"
            return render_template("admin.html", error=msg)
        finally:
            dbClose()
        return render_template("admin.html")
    return render_template("admin.html")

@app.route("/adlogin", methods = ['POST', 'GET'])
def adlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'] 

        # print(email)
        # print(password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM admin WHERE email = %s AND pass = %s', (email, password))
        result = cursor.fetchone()
        print("result")
        print(result)
        if result_count>0:
            print("len of result")
            session['uname'] = result[1]
            session['userid'] = result[0]
            return redirect(url_for('adhome'))
        else:
            return render_template('admin.html')
    return render_template('admin.html')

@app.route("/adhome")
def adhome():
    if 'uname' in session:
        global final_data
        print(" hii root")
        username=session.get('uname')
        con = dbConnection()
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM user_analysis")
        result1 = cursor.fetchall()
        print("### result1 ###")
        print(result1)
        con.commit()   
        user_data = list(result1)

        sr_no=[]
        prdct_id=[]
        prdct_name=[]
        uname=[]
        cmnts=[]
        ipad=[]
        real_fk=[]
        tim_stmp=[]
        by_not=[]
        rprt_count=[]
        for i in user_data:
            a=i[0]
            print("### printing a ###")
            print(a)
            sr_no.append(a)

            b=i[1]
            prdct_id.append(b)

            c=i[2]
            prdct_name.append(c)

            d=i[3]
            uname.append(d)

            e=i[4]
            cmnts.append(e)

            f=i[5]
            ipad.append(f)

            g=i[6]
            real_fk.append(g)

            h=i[7]
            tim_stmp.append(h)

            l=i[8]
            by_not.append(l)

            j=i[9]
            rprt_count.append(j)
        
        final_data=zip(sr_no,prdct_id,prdct_name,uname,cmnts,ipad,real_fk,tim_stmp,by_not,rprt_count)
        return render_template('adhome.html',  firstName=username, final_data=final_data)
    return render_template('adhome.html')

@app.route("/analysis")
def analysis():
    if 'uname' in session:
        print(" hii root")
        username=session.get('uname')
        con = dbConnection()
        cur = con.cursor()
        cur.execute("select * from user_analysis")
        result = cur.fetchall()
        result = list(result)
        product_id = []
        product_name = []
        uname = []
        comments = []
        ipadd = []
        nb_real_fake = []
        svm_real_fake = []
        rf_real_fake = []
        time_stmp = []
        buy1_not0 = []
        report = []

        for i in result:
            a = i[1]
            product_id.append(a)
            b = i[2]
            product_name.append(b)
            c = i[3]
            uname.append(c)
            d = i[4]
            comments.append(d)
            e = i[5]
            ipadd.append(e)
            f = i[6]
            nb_real_fake.append(f)
            g = i[7]
            svm_real_fake.append(g)
            h = i[8]
            rf_real_fake.append(h)
            j = i[9]
            time_stmp.append(j)
            k = i[10]
            buy1_not0.append(k)
            l = i[11]
            report.append(l)

        flst = zip(product_id,product_name,uname,comments,ipadd,nb_real_fake,svm_real_fake,rf_real_fake,time_stmp,buy1_not0,report)

        final_score=[]
        for product_id,product_name,uname,comments,ipadd,nb_real_fake,svm_real_fake,rf_real_fake,time_stmp,buy1_not0,report in flst:
            umarks = []
            print()
            print(product_id,product_name,uname,comments,ipadd,nb_real_fake,svm_real_fake,rf_real_fake,time_stmp,buy1_not0,report)
            print()

            # Algorithms to identify fake and correct will used
            if nb_real_fake == "Fake" and svm_real_fake == "Fake" and rf_real_fake == "Fake":
                a = 20+20+20
                umarks.append(a)
            elif nb_real_fake == "Real" and svm_real_fake == "Fake" and rf_real_fake == "Fake":
                a = 0+20+20
                umarks.append(a)
            elif nb_real_fake == "Fake" and svm_real_fake == "Real" and rf_real_fake == "Fake":
                a = 20+0+20
                umarks.append(a)
            elif nb_real_fake == "Fake" and svm_real_fake == "Fake" and rf_real_fake == "Real":
                a = 20+20+0
                umarks.append(a)
            else:
                a = 0+0+0
                umarks.append(a)

            cur.execute("select uname,time_stmp,comments from user_analysis where ipadd=%s",(ipadd))
            unameres = cur.fetchall()
            unameres = list(unameres)

            if len(comments)>0 and len(unameres)>1 and buy1_not0 == "0" and report=="1":
                b = 10+10+10+10
                umarks.append(b)
            elif len(comments)>0 and len(unameres)>1 and buy1_not0 == "1" and report=="0":
                b = 10+10+0
                umarks.append(b)
            else:
                b = 0+0+0
                umarks.append(b)

            final_score.append(umarks)
            print()
            print("printing umarks list: ",umarks)
            print()
            print("printing sum of umarks: ",sum(umarks))
            print()
            sum_score = sum(umarks)
            
            ftag = ""
            if sum_score>=70:
                ftag+="Fake"
            else:
                ftag+="Real"

            sql = "INSERT INTO final_score(product_id,product_name,uname,comments,ipadd,nb_real_fake,svm_real_fake,rf_real_fake,time_stmp,buy1_not0,report,final_sum,final_tag) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (product_id,product_name,uname,comments,ipadd,nb_real_fake,svm_real_fake,rf_real_fake,time_stmp,buy1_not0,report,sum_score,ftag)
            cur.execute(sql,val)
            con.commit()
        
        con = dbConnection()
        cur = con.cursor()
        cur.execute("select * from final_score")
        result = cur.fetchall()
        result = list(result)
        product_id = []
        product_name = []
        uname = []
        comments = []
        ipadd = []
        nb_real_fake = []
        svm_real_fake = []
        rf_real_fake = []
        time_stmp = []
        buy1_not0 = []
        report = []
        score_sum = []
        final_tag = []
        uid = []

        for i in result:
            x = i[0]
            uid.append(x)
            a = i[1]
            product_id.append(a)
            b = i[2]
            product_name.append(b)
            c = i[3]
            uname.append(c)
            d = i[4]
            comments.append(d)
            e = i[5]
            ipadd.append(e)
            f = i[6]
            nb_real_fake.append(f)
            g = i[7]
            svm_real_fake.append(g)
            h = i[8]
            rf_real_fake.append(h)
            j = i[9]
            time_stmp.append(j)
            k = i[10]
            buy1_not0.append(k)
            l = i[11]
            report.append(l)
            m = i[12]
            score_sum.append(m)
            n = i[13]
            final_tag.append(n)

        flst1 = zip(uid,product_id,product_name,uname,comments,ipadd,nb_real_fake,svm_real_fake,rf_real_fake,time_stmp,buy1_not0,report,score_sum,final_tag)

        return render_template('analysis2.html',  firstName=username,flst1=flst1)
    return render_template('login.html')


if __name__=='__main__':
    app.run(debug=True)
    # app.run('0.0.0.0')