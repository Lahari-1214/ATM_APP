from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('register.html')

@app.route('/create',methods=['POST'])
def Create():
    acc_no = request.form.get('acc_no')
    username = request.form.get('username')
    balance = request.form.get('balance')
    return redirect(url_for('Dashboard',acc_no=acc_no,username=username,balance=balance))
@app.route('/dashboard')
def Dashboard():
    acc_no = request.args.get('acc_no')
    username = request.args.get('username')
    balance = request.args.get('balance')
    return render_template('dashboard.html', acc_no=acc_no,
        username=username,
        balance=balance)


if __name__ == '__main__':
    app.run(debug=True)