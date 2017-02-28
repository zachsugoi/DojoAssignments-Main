import re
from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'mydb')
app.secret_key = 'SecretKeyNumber7000'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register', methods=['POST'])
def register():
    if (len(request.form['first_name']) >= 2 and
            str.isalpha(str(request.form['first_name'])) == True and
            len(request.form['last_name']) >= 2 and
            str.isalpha(str(request.form['last_name'])) == True and
            EMAIL_REGEX.match(request.form['email']) and
            len(request.form['password']) >= 8 and
            request.form['pass_conf'] == request.form['password']):
        bcrypt_pass = bcrypt.generate_password_hash(request.form['password'])
        query = """INSERT INTO login (first_name, last_name, email, pw_hash, created_at, updated_at)
                VALUES (:first_name, :last_name, :email, :bcrypt_pass, NOW(), NOW())"""
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'bcrypt_pass': bcrypt_pass
                }
        mysql.query_db(query, data)
        flash('Registration Successful. Now, please log in to the right.','success')
        return redirect('/')
    if len(request.form['first_name']) < 2:
        flash('Name must be at least 2 letters','first_name')
    if not str.isalpha(str(request.form['first_name'])) and len(request.form['first_name']) >= 2:
        flash('Name must only include letters','first_name')
    if len(request.form['last_name']) < 2:
        flash('Name must be at least 2 letters','last_name')
    if not str.isalpha(str(request.form['last_name'])) and len(request.form['last_name']) >= 2:
        flash('Name must only include letters','last_name')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Improper email format','email')
    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters','password')
    if request.form['pass_conf'] != request.form['password']:
        flash('Password confirm does not match password','pass_conf')
    return redirect('/')
@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM login WHERE email = :email"
    data = {
            'email': request.form['email']
            }
    user = mysql.query_db(query, data)
    if user:
        if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
            session['first_name'] = user[0]['first_name']
            session['last_name'] = user[0]['last_name']
            return render_template('success.html')
        else:
            flash('Invalid Password','invalid_pass')
            return redirect('/')
    else:
        flash('Email does not match our records. Please try again or register.','invalid_email')
        return redirect('/')
app.run(debug=True)
