import re
from flask import Flask, redirect, request, flash, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'IveABigOlSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'email_validation')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check', methods=['POST'])
def check():
    if not EMAIL_REGEX.match(request.form['email_address']):
        flash('Email is not valid!')
        return redirect('/')
    else:
        session['submitted_email'] = request.form['email_address']
        query = """INSERT INTO email_addresses (email_address, created_at, updated_at)
                VALUES (:email_address, NOW(), NOW())"""
        data = {
                'email_address': request.form['email_address']
                }
        mysql.query_db(query, data)
        return redirect('/success')
@app.route('/success')
def success():
    query = "SELECT email_address, DATE_FORMAT(updated_at,'%m/%d/%Y %I:%i%p') AS updated_at FROM email_addresses"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)
@app.route('/delete', methods=['POST'])
def delete():
    query = "DELETE FROM email_addresses WHERE email_address = :del_email"
    data = {
            'del_email': request.form['del_email']
            }
    mysql.query_db(query, data)
    return redirect('/success')
app.run(debug=True)
