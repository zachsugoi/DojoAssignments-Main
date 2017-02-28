import re
from flask import Flask, redirect, render_template, request, flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'FlashApparentlyNeedsAPasswordToo'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check', methods=['POST'])
def check():
    if len(request.form['email']) < 1:
        flash('Email address required','email')
    if len(request.form['first_name']) < 1:
        flash('First name required','first_name')
    if len(request.form['last_name']) < 1:
        flash('Last name required','last_name')
    if len(request.form['password']) < 1:
        flash('Password required','password')
    if len(request.form['confirm_pass']) < 1:
        flash('Password confirmation required','confirm_pass')
    if str.isalpha(str(request.form['first_name'])) == False and len(request.form['first_name']) > 0:
        flash('Name cannot contain numbers','first_name')
    if str.isalpha(str(request.form['last_name'])) == False and len(request.form['last_name']) > 0:
        flash('Name cannot contain numbers','last_name')
    if len(request.form['password']) < 8 and len(request.form['password']) > 0:
        flash('Password must be at least 8 characters','password')
    if not EMAIL_REGEX.match(request.form['email']) and len(request.form['email']) > 0:
        flash('Invalid email address','email')
    if request.form['password'] != request.form['confirm_pass']:
        flash('Does not match password','confirm_pass')
    if (len(request.form['email']) > 0 and
        len(request.form['first_name']) > 0 and
        len(request.form['last_name']) > 0 and
        len(request.form['password']) > 0 and
        str.isalpha(str(request.form['first_name'])) == True and
        str.isalpha(str(request.form['last_name'])) == True and
        len(request.form['password']) > 7 and
        EMAIL_REGEX.match(request.form['email']) and
        request.form['password'] == request.form['confirm_pass']):
        flash('Registration complete!','success')
    return redirect('/')
app.run(debug=True)
