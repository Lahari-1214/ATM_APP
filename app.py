from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
app = Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="leela@123",database="ATM_DB")
# accounts={}
@app.route('/')
def Home():
    return render_template('register.html')

@app.route("/create", methods=["POST"])
def create_account():
    acc_no = request.form["acc_no"]
    name = request.form["name"]
    balance = int(request.form["balance"])
    pin = request.form["pin"]
    query = """
       INSERT INTO accounts (acc_no, name, initial_balance, pin)
        VALUES (%s, %s, %s,%s)
    """
    cursor = db.cursor()
    cursor.execute(query, (acc_no, name, balance,pin))
    db.commit()
    return redirect(url_for("Dashboard", acc_no=acc_no))
# DASHBOARD
# @app.route("/dashboard/<acc_no>")
@app.route("/dashboard/<int:acc_no>")
def Dashboard(acc_no):
    cursor = db.cursor()
    query = "SELECT * FROM accounts WHERE acc_no = %s"
    cursor.execute(query, (acc_no,))
    account = cursor.fetchone()

    if not account:
        return "Account not found"

    return render_template(
        "dashboard.html",
        acc_no=account[0],
        name=account[1],
        balance=account[2]
    )

# DEPOSIT
@app.route("/deposit/<int:acc_no>", methods=["POST"])
def deposit(acc_no):
    amount = float(request.form["amt"])
    cursor = db.cursor()

    query = """
        UPDATE accounts
        SET initial_balance = initial_balance + %s
        WHERE acc_no = %s
    """
    cursor.execute(query, (amount, acc_no))
    db.commit()

    return redirect(url_for("Dashboard", acc_no=acc_no))


@app.route('/withdraw/<acc_no>',methods=['POST'])
@app.route("/withdraw/<int:acc_no>", methods=["POST"])
def Withdraw(acc_no):
    amount = float(request.form["amt"])
    cursor = db.cursor()

    cursor.execute(
        "SELECT initial_balance FROM accounts WHERE acc_no = %s",
        (acc_no,)
    )
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute(
            "UPDATE accounts SET initial_balance = initial_balance - %s WHERE acc_no = %s",
            (amount, acc_no)
        )
        db.commit()
        return redirect(url_for("Dashboard", acc_no=acc_no))
    else:
        return "Insufficient balance" #wanted to make this update using javascript 

    
# DELETE ACCOUNT
@app.route("/delete/<int:acc_no>")
def delete(acc_no):
    cursor = db.cursor()
    cursor.execute("DELETE FROM accounts WHERE acc_no = %s", (acc_no,))
    db.commit()
    return redirect(url_for("Home"))


# Login Page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        acc_no = request.form['acc_no']
        pin = request.form['pin']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM accounts WHERE acc_no = %s AND pin = %s", (acc_no, pin))
        account = cursor.fetchone()

        if account:
            return redirect(url_for('Dashboard', acc_no=acc_no))
        else:
            return "Invalid account number or PIN"

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)




