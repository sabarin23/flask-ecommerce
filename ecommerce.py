from flask import Flask, render_template, request, session, redirect, url_for, flash

try:
    import MySQLdb
except:
    import pymysql as MySQLdb
import os	
app = Flask(__name__, template_folder='templates')
APP_ROOT=os.path.dirname(os.path.abspath(__file__))
app.secret_key = 'this is secret_key'
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/registered/<name>')
def registered(name):
    return render_template("index.html")

@app.route('/logged_in/<name>')
def logged_in(name):
    return render_template("index.html")

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method=='POST':
        conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "root")
        c = conn.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS `mydb`")
        c.execute("USE mydb")
        c.execute("CREATE TABLE IF NOT EXISTS `reg` (`uname` varchar(45) NOT NULL, `email` varchar(45) NOT NULL, `pass` varchar(45) NOT NULL, `cpass` varchar(45) NOT NULL, PRIMARY KEY (`email`))")
        uname=request.form['uname']
        email=request.form['email']
        passs=request.form['pass']
        cpasss=request.form['cpass']
        c.execute("Insert into reg(uname,email,pass,cpass) values(%s,%s,%s,%s)",(uname,email,passs,cpasss))
        data=uname
        conn.commit()
        conn.close()
        return redirect(url_for('registered', name=uname))
        #return render_template("index.html", data=data)

@app.route("/signin",methods=['POST','GET'])
def signin():
    if request.method=='POST':
        print(request.form)
        uname=request.form['uname']
        passs=request.form['pass']
        conn = MySQLdb.connect(host="localhost",
                               user = "root",
                               passwd = "root",
                               db = "mydb")
        c = conn.cursor()
        c.execute("SELECT * FROM `reg` WHERE (`uname` = %s or `email` = %s) and pass = %s", [uname,uname,passs])
        data1 = c.fetchone()
        if data1 == None:
            return render_template('index.html')
        else:
            return redirect(url_for('logged_in', name=uname))

@app.route("/logout",methods=['POST','GET'])
def logout():
    session.pop('username')
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/product")
def product():
    return render_template("product.html")


@app.route("/product2")
def product2():
    return render_template("product2.html")

@app.route("/single")
def single():
    return render_template("single.html")


@app.route("/single2")
def single2():
    return render_template("single2.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/typography")
def typography():
    return render_template("typography.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/icons")
def icons():
    return render_template("icons.html")


if __name__ == "__main__":
    app.run(debug=True)
