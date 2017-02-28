import re
from flask import Flask, redirect, request, render_template, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'Secretious'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    session['current_id'] = ''
    session['first_name'] = ''
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
        query = """INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at)
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
    query = "SELECT * FROM users WHERE email = :email"
    data = {
            'email': request.form['email']
            }
    user = mysql.query_db(query, data)
    if user:
        if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
            session['current_id'] = user[0]['id']
            session['first_name'] = user[0]['first_name']
            return redirect('/wall')
        else:
            flash('Invalid Password','invalid_pass')
            return redirect('/')
    else:
        flash('Email does not match our records. Please try again or register.','invalid_email')
        return redirect('/')
@app.route('/wall')
def wall():
    query_messages = """SELECT DISTINCT messages.user_id, users.first_name, users.last_name,
                            messages.id AS message_id, messages.message,
                            DATE_FORMAT(messages.created_at,'%M %D %Y') AS created_at
                        FROM messages INNER JOIN users ON users.id = messages.user_id
                        ORDER BY messages.created_at DESC"""
    all_messages = mysql.query_db(query_messages)
    all_messages_w_comments = []
    for message in all_messages:
        query_comments = """SELECT DISTINCT comments.user_id AS comment_user_id, users.first_name AS comment_first_name,
                                users.last_name AS comment_last_name, comments.id AS comment_id, comments.comment,
                                DATE_FORMAT(comments.created_at, '%b %D %Y') AS comment_created_at
                            FROM comments
                            INNER JOIN users
                                ON users.id = comments.user_id
                            WHERE comments.message_id = :message_id
                            ORDER BY comments.created_at"""
        data_comments = {
                        'message_id': message['message_id']
                        }
        comments = mysql.query_db(query_comments, data_comments)
        message_w_comments = []
        message_w_comments.append(message)
        message_w_comments.append(comments)
        all_messages_w_comments.append(message_w_comments)
    return render_template('wall.html', all_messages_w_comments=all_messages_w_comments)
@app.route('/message', methods=['POST'])
def message():
    if request.form['message'] == '':
        return redirect('/wall')
    else:
        query = """INSERT INTO messages (user_id, message, created_at, updated_at)
                    VALUES (:user_id, :message, NOW(), NOW())"""
        data = {
                'user_id': session['current_id'],
                'message': request.form['message']
                }
        mysql.query_db(query, data)
        return redirect('/wall')
@app.route('/comment', methods=['POST'])
def comment():
    if request.form['comment'] == '':
        return redirect('/wall')
    else:
        query = """INSERT INTO comments (message_id, user_id, comment, created_at, updated_at)
                    VALUES (:message_id, :user_id, :comment, NOW(), NOW())"""
        data = {
                'message_id': request.form['message_id'],
                'user_id': session['current_id'],
                'comment': request.form['comment']
                }
        mysql.query_db(query, data)
        return redirect('/wall')
@app.route('/deletecomment', methods=['POST'])
def delete_comment():
    query = "DELETE FROM comments WHERE id = :id"
    data = {
            'id': request.form['comment_id']
            }
    mysql.query_db(query, data)
    return redirect('/wall')
app.run(debug=True)
