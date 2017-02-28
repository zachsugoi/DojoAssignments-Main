import random, datetime
from flask import Flask, render_template, request, redirect, session, Markup
app = Flask(__name__)
app.secret_key = 'NinjaInDaHouse'
@app.route('/')
def index():
    if not 'bank' in session:
        session['bank'] = 0
    if not 'log' in session:
        session['log'] = ''
    return render_template('ninja_money.html')
@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        increase = random.randrange(10,21)
        session['bank'] += increase
        session['log'] += Markup("<p class='earn'>Earned "+str(increase)+" golds from the farm! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>")
        return redirect('/')
    elif request.form['building'] == 'cave':
        increase = random.randrange(5,11)
        session['bank'] += increase
        session['log'] += Markup("<p class='earn'>Earned "+str(increase)+" golds from the cave! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>")
        return redirect('/')
    elif request.form['building'] == 'house':
        increase = random.randrange(2,6)
        session['bank'] += increase
        session['log'] += Markup("<p class='earn'>Earned "+str(increase)+" golds from the house! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>")
        return redirect('/')
    elif request.form['building'] == 'casino':
        increase = random.randrange(-50,51)
        session['bank'] += increase
        if increase > 0:
            session['log'] += Markup("<p class='earn'>Earned "+str(increase)+" golds from the casino! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>")
        else:
            session['log'] += Markup("<p class='lose'>Entered a casino and lost "+str(abs(increase))+" golds... Ouch.. "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>")
        return redirect('/')
@app.route('/restart', methods=['POST'])
def restart():
    session['bank'] = 0
    session['log'] = ''
    return redirect('/')
app.run(debug=True)
