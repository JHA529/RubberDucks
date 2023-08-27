from flask import *
from forms import BasicForm
import pymysql


app = Flask(__name__)
app.config['SECRET_KEY']='woop'

def connection():
    server = 'localhost'
    db = 'rubberducks'
    uid = 'sky'
    pwd = 'P@$$word'
    conn = pymysql.connect(host=server, user=uid, password=pwd, database=db)
    conn.autocommit(True)
    return conn

@app.route('/addcustomer', methods = ['GET', 'POST'])
def addcustomer():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]

        conn = connection()
        cursor = conn.cursor()
        cursor.execute("insert into customers (firstname, lastname, email) values('"+firstname+"','"+lastname+"','"+email+"')")
        return "Customer successfully added"
    return render_template("addcustomer.html")

@app.route('/addorder', methods = ['GET', 'POST'])
def addorder():
    if request.method == "POST":
        dish = request.form["dish"]
        eventname = request.form["eventname"]
        eventdate = request.form["eventdate"]

        conn = connection()
        cursor = conn.cursor()
        cursor.execute("insert into orders (dish, eventname, eventdate) values('" + dish + "','" + eventname + "','" + eventdate + "')")
        return "Order successfully added"
    return render_template("addorder.html")





if __name__=="__main__":
    app.run()
