from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/shares', methods = ['GET', 'POST'])
def shares():
    if request.method == "GET":
        return "Please fill out the form."
    else:
        userdata = dict(request.form)
        all_shares = model.shares_calculator(userdata['symbol'], float(userdata['Balance']), userdata['yearbuying'])
        return render_template('shares.html', all_shares = all_shares, initial_year = userdata['yearbuying'], initial_balance = float(userdata['Balance']), symbol = userdata['symbol'])
        

@app.route('/finalbalance', methods = ['GET', 'POST'])
def finalbalance():
    if request.method == "GET":
        return "Please fill out the form."
    else:
        userdata = dict(request.form)
        total_sharesfinal = float(userdata['all_shares'])
        print("Ok")
        final_balance = model.balance_calculator(total_sharesfinal, float(userdata['shares']), userdata['symbol'], float(userdata['initial_balance']), userdata['initial_year'], userdata['yearselling'])
        return render_template('finalbalance.html', finalbalance = final_balance, symbol = userdata['symbol'])