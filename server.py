from flask import Flask, render_template, redirect, request, session
import random
import datetime
app = Flask(__name__)
app.secret_key="shiro"

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold']=0
    if not 'activities' in session:
        session['activities'] =""
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def submit():
    timestamp = str(datetime.datetime.now().strftime('%b %Y %I:%M%p'))
    rgb = "green"
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        session['activities'] += "Earned " + str(gold) + " golds from the "+ request.form['building'] + "! ("+timestamp+") \r"
        session['gold'] += gold
        return redirect('/')

    if request.form['building'] == 'cave':
        gold = random.randrange(5,11)
        session['gold'] += gold
        session['activities'] += "Earned " + str(gold) + " golds from the "+ request.form['building'] + "! ("+timestamp+") \r"
        return redirect('/')

    if request.form['building'] == 'house':
        gold = random.randrange(2,6)
        session['gold'] += gold
        session['activities'] += "Earned " + str(gold) + " golds from the "+ request.form['building'] + "! ("+timestamp+") \r"
        return redirect('/')

    if request.form['building'] == 'casino':
        gold = random.randint(-50,51)
        session['gold'] += gold
        if gold>=0:
            session['activities'] += "Entered a casino and won " +str(gold)+ " golds! (" +timestamp+")\r"

        else:
            rgb = "red"
            session['activities'] += "Entered a casino and lost " +str(gold)+ " golds... Ouch.. (" +timestamp+")\r"
        return redirect ('/')

@app.route('/reset')
def reset():
    print "Hit Route"
    session.pop('gold')
    session.pop('activities')
    return redirect('/')

app.run(debug=True)