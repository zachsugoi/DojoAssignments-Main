import re
from flask import Flask, redirect, request, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'Secretious'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM full_friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    if request.form['first_name'] != '' and request.form['last_name'] != '' and EMAIL_REGEX.match(request.form['email']):
        query = """INSERT INTO full_friends (first_name, last_name, email, created_at, updated_at)
                    VALUES (:first_name, :last_name, :email, NOW(), NOW())"""
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email']
                }
        mysql.query_db(query, data)
        return redirect('/')
    if request.form['first_name'] == '' or request.form['last_name'] == '':
        flash('Must provide both a first and last name')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Must provide valid email address')
    return redirect('/')
@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM full_friends WHERE id = :id"
    data = {
            'id': id
            }
    edit_friend = mysql.query_db(query, data)[0]
    return render_template('edit.html', edit_friend=edit_friend)
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = """UPDATE full_friends
                SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW()
                WHERE id = :id"""
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
            }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/friends/<id>/delete', methods=['POST']) #the assignment says to make this route POST, but I don't believe it's necessary
def destroy(id):
    query = "DELETE FROM full_friends WHERE id = :id"
    data = {
            'id': id
            }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
