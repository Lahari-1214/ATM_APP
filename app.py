from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
app = Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="leela@123",database="ATM_DB")
accounts={}
@app.route('/')
def Home():
    return render_template('register.html')

@app.route("/create", methods=["POST"])
def create_account():
    acc_no = request.form["acc_no"]
    name = request.form["name"]
    balance = int(request.form["balance"])
    accounts[acc_no] = {"name": name, "balance": balance}
    return redirect(url_for("Dashboard", acc_no=acc_no))
# DASHBOARD
@app.route("/dashboard/<acc_no>")
def Dashboard(acc_no):
    data = accounts[acc_no]
    return render_template("dashboard.html", acc_no=acc_no, data=data)
# DEPOSIT
@app.route("/deposit/<acc_no>", methods=["POST"])
def deposit(acc_no):
    amount = int(request.form["amt"])
    if amount>0:
        accounts[acc_no]["balance"] += amount
        return redirect(url_for("Dashboard", acc_no=acc_no))
    return "Invalid Amount"

@app.route('/withdraw/<acc_no>',methods=['POST'])
def Withdrawn(acc_no):
    amount = int(request.form['amt'])  # Get withdrawal amount

    if accounts[acc_no]['balance'] >= amount:
        accounts[acc_no]['balance'] -= amount  # Deduct from balance
        # return redirect(url_for("dashboard", acc_no=acc_no))
        return redirect(url_for('Dashboard',acc_no=acc_no))
    else:
        # If insufficient balance, show message with link to go back
        return f'Insufficient balance'
    
# DELETE ACCOUNT
@app.route("/delete/<acc_no>")
def delete(acc_no):
    accounts.pop(acc_no)
    return redirect(url_for("Home"))

if __name__ == '__main__':
    app.run(debug=True)