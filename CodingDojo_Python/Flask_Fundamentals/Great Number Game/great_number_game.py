import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'BigOSecret'
@app.route('/')
def index():
    session['randnum'] = random.randrange(0,101)
    print session['randnum']
    return render_template('index.html')
@app.route('/discern', methods=['POST'])
def discern():
    session['guess'] = int(request.form['guess'])
    if session['guess'] < session['randnum']:
        return render_template('low.html')
    elif session['guess'] > session['randnum']:
        return render_template('high.html')
    elif session['guess'] == session['randnum']:
        return render_template('nice.html')
app.run(debug=True)
