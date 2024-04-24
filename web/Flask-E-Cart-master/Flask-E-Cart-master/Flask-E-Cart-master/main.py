from flask import *
import sqlite3,hashlib, os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

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

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'random string'
##########################################################################################################
#                                   Fetching details from database
##########################################################################################################
def getLoginDetails():
    cur = con.cursor()
    if 'firstName' not in session:
        print("getLoginDetails if")
        loggedIn = False
        firstName = ''
        noOfItems = 0
    else:
        print("getLoginDetails else")
        loggedIn = True
        sql1 = ("SELECT userId, firstName FROM users WHERE email = %s")
        val = (session['email'])
        cursor.execute(sql1, val)
        userId, firstName = cur.fetchone()
        sql2 = ("SELECT count(productId) FROM kart WHERE userId = %s")
        val2 = (str(userId))
        cursor.execute(sql2, val2)
        noOfItems = cur.fetchone()[0]
        con.commit()
        con.close()
    return (loggedIn, firstName, noOfItems) 
##########################################################################################################
#                                           Register
##########################################################################################################
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #Parse form data    
        print("hii register")
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
        firstName = request.form['firstName']

        print(cpassword)
        try: 
            con = dbConnection()
            cursor = con.cursor()
            sql = "INSERT INTO users (firstName, email, pass) VALUES (%s, %s, %s)"
            val = (firstName, email, password)
            cursor.execute(sql, val)
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
def is_valid(email, password):
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT email, pass FROM users')
    result = cursor.fetchone()
    print("result")
    print(result)
    for row in result:
        if row[0] == email and row[1] == password:
            return True
    return False

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s AND pass = %s', (email, password))
        result = cursor.fetchone()
        print("result")
        print(result)
        if len(result)>0:
            print("len of result")
            session['uname'] = result[1]
            session['userid'] = result[0]
            return redirect(url_for('root'))
        else:
            return render_template('login.html')
    return render_template('login.html')
##########################################################################################################
#                                   Inserting product in database
##########################################################################################################
@app.route("/")
def root():
    loggedIn, firstName, noOfItems = getLoginDetails()

    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT productId, name, price, description, image, stock FROM products")
    result1 = cursor.fetchone()
    cursor.execute("SELECT categoryId, name FROM categories")
    categoryData = cursor.fetchone()
    con.commit()
    # itemData = parse(result1)   

    return render_template('home.html', loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems, categoryData=categoryData)


@app.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('root'))
    else:
        return render_template('login.html', error='')


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/registerationForm")
def registrationForm():
    return render_template("register.html")

@app.route("/add")
def admin():
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT categoryId, name FROM categories")
        categories = cur.fetchall()
    conn.close()
    return render_template('add.html', categories=categories)


def parse(data):
    ans = []
    i = 0
    while i < len(data):
        curr = []
        for j in range(7):
            if i >= len(data):
                break
            curr.append(data[i])
            i += 1
        ans.append(curr)
    return ans

@app.route("/addItem", methods=["GET", "POST"])
def addItem():
    if request.method == "POST":
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form['description']
        categoryId = int(request.form['category'])

        #Uploading image procedure
        image = request.files['image']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imagename = filename
        with sqlite3.connect('base.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO products (name, price, description, image, categoryId) VALUES (?, ?, ?, ?, ?)''', (name, price, description, imagename, categoryId))
                conn.commit()
                msg="added successfully"
            except:
                msg="error occured"
                conn.rollback()
        conn.close()
        print(msg)
        return redirect(url_for('root'))

@app.route("/remove")
def remove():
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT productId, name, price, description FROM products')
        data = cur.fetchall()
    conn.close()
    return render_template('remove.html', data=data)

@app.route("/removeItem")
def removeItem():
    productId = request.args.get('productId')
    with sqlite3.connect('base.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM products WHERE productID = ' + productId)
            conn.commit()
            msg = "Deleted successsfully"
        except:
            conn.rollback()
            msg = "Error occured"
    conn.close()
    print(msg)
    return redirect(url_for('root'))
@app.route("/displayCategory")
def displayCategory():
        loggedIn, firstName, noOfItems = getLoginDetails()
        categoryId = request.args.get("categoryId")
        with sqlite3.connect('base.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT products.productId, products.name, products.price, products.image, categories.name FROM products, categories WHERE products.categoryId = categories.categoryId AND categories.categoryId = " + categoryId)
            data = cur.fetchall()
        conn.close()
        categoryName = data[0][4]
        data = parse(data)
        return render_template('displayCategory.html', data=data, loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems, categoryName=categoryName)


@app.route("/productDescription")
def productDescription():
    loggedIn, firstName, noOfItems = getLoginDetails()
    productId = request.args.get('productId')
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT productId, name, price, description, image, stock FROM products WHERE productId = ' + productId)
        productData = cur.fetchone()
    conn.close()
    return render_template('item.html', data=productData, loggedIn = loggedIn, firstName = firstName, noOfItems = noOfItems)


@app.route("/addToCart")
def addToCart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    else:
        productId = int(request.args.get('productId'))
        with sqlite3.connect('base.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId FROM users WHERE email = '" + session['email'] + "'")
            userId = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO kart (userId, productId) VALUES (?, ?)", (userId, productId))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return redirect(url_for('root'))


@app.route("/removeFromCart")
def removeFromCart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    email = session['email']
    productId = int(request.args.get('productId'))
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT userId FROM users WHERE email = '" + email + "'")
        userId = cur.fetchone()[0]
        try:
            cur.execute("DELETE FROM kart WHERE userId = " + str(userId) + " AND productId = " + str(productId))
            conn.commit()
            msg = "removed successfully"
        except:
            conn.rollback()
            msg = "error occured"
    conn.close()
    return redirect(url_for('root'))


@app.route("/cart")
def cart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    loggedIn, firstName, noOfItems = getLoginDetails()
    email = session['email']
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT userId FROM users WHERE email = '" + email + "'")
        userId = cur.fetchone()[0]
        cur.execute("SELECT products.productId, products.name, products.price, products.image FROM products, kart WHERE products.productId = kart.productId AND kart.userId = " + str(userId))
        products = cur.fetchall()
    totalPrice = 0
    for row in products:
        totalPrice += row[2]
    return render_template("cart.html", products = products, totalPrice=totalPrice, loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems)


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('root'))


@app.route("/prod")
def prodp():
    loggedIn, firstName, noOfItems = getLoginDetails()
    return render_template('product.html',loggedIn = loggedIn, firstName = firstName, noOfItems = noOfItems)


@app.route("/account/profile/changePassword", methods=["GET", "POST"])
def changePassword():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    if request.method == "POST":
        oldPassword = request.form['oldpassword']
        oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
        newPassword = request.form['newpassword']
        newPassword = hashlib.md5(newPassword.encode()).hexdigest()
        with sqlite3.connect('base.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, password FROM users WHERE email = '" + session['email'] + "'")
            userId, password = cur.fetchone()
            if (password == oldPassword):
                try:
                    cur.execute("UPDATE users SET password = ? WHERE userId = ?", (newPassword, userId))
                    conn.commit()
                    msg="Changed successfully"
                except:
                    conn.rollback()
                    msg = "Failed"
                return render_template("recover.html", msg=msg)
            else:
                msg = "Wrong password"
        conn.close()
        return render_template("recover.html", msg=msg)
    else:
        return render_template("recover.html")


@app.route("/address", methods = ['GET', 'POST'])
def bill():
    if request.method == 'POST':
        #Parse form data    
        email = request.form['email']
        address = request.form['address']
        postcode = request.form['postcode']
        mobile = request.form['mobile']
        

        with sqlite3.connect('base.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO address (email,address,postcode,mobile) VALUES (?, ?, ?, ?)', (email,address,postcode,mobile))
                con.commit()
                msg = "Thank you"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return render_template('bill.html', error=msg)


@app.route("/bill")
def address():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    loggedIn, firstName, noOfItems = getLoginDetails()
    email = session['email']
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT userId FROM users WHERE email = '" + email + "'")
        userId = cur.fetchone()[0]
        cur.execute("SELECT products.productId, products.name, products.price, products.image FROM products, kart WHERE products.productId = kart.productId AND kart.userId = " + str(userId))
        products = cur.fetchall()
    totalPrice = 0
    for row in products:
        totalPrice += row[2]
    return render_template("bill.html",loggedIn = loggedIn, firstName = firstName, noOfItems = noOfItems,products = products, totalPrice=totalPrice)
@app.route("/end")
def last():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    loggedIn, firstName, noOfItems = getLoginDetails()
    email = session['email']
    with sqlite3.connect('base.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT userId FROM users WHERE email = '" + email + "'")
        userId = cur.fetchone()[0]
        cur.execute("SELECT products.productId, products.name, products.price, products.image FROM products, kart WHERE products.productId = kart.productId AND kart.userId = " + str(userId))
        products = cur.fetchall()
    return render_template('end.html',products = products, loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems)

if __name__=='__main__':
    app.run('0.0.0.0')





































