from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'SecretsMakeTheWorldGoRound'
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/results', methods=['POST'])
def results():
    print "Got Post Info"
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
        return render_template('index.html')
    elif len(request.form['comment']) < 1:
        flash("Even though it says it's optional, you must leave a comment.")
        return render_template('index.html')
    elif len(request.form['comment']) > 120:
        flash('Geez, Chatty Cathy! Keep your comments brief!')
        return render_template('index.html')
    else:
        return render_template("results.html", name=request.form["name"], location=request.form["location"], language=request.form["language"], comment=request.form["comment"])
app.run(debug=True)
