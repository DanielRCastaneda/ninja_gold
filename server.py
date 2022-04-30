from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
import random 
app.secret_key = 'qwerty'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    session['activity'].insert( 0,'game begin')
    
    return render_template('index.html', gold = session['gold'],  activity = session['activity'])

@app.route('/process', methods=['POST'])
def process():
    if request.form['building'] == 'casino':
        gold = random.randint(0,50)
        if random.randint(1, 4)%2 == 1:
            session['gold'] -= gold
            session['activity'].insert(1, f"Entered a casino and lost {gold} golds.. Ouch..")
        else:
            session['gold'] += gold
            session['activity'].insert(2,f"Entered a casino and WON {gold} golds!")
    else:
        if request.form['building'] == 'house':
            gold = random.randint(2,5)
        if request.form['building'] == 'cave':
            gold = random.randint(5,10)
        if request.form['building'] == 'farm':
            gold = random.randint(10,20)
        session['gold'] += gold
        session['activity'].insert(2,f"Entered a casino and WON {gold} golds!")
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":     
    app.run(debug=True) 