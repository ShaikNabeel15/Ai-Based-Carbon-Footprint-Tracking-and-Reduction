from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import sys

# Add project root to sys.path to allow imports from backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.auth import signup_user, login_user
from backend.carbon_logic import update_carbon_produced, get_sellers, buy_carbon, set_selling_info
from backend.ai_agent import get_ai_suggestions, get_admin_summary
from backend.database import get_factories, get_transactions

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        result = signup_user(data['factory_name'], data['factory_id'], data['email'], data['password'])
        if "success" in result:
            return redirect(url_for('login'))
        return render_template('signup.html', error=result['error'])
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        result = login_user(data['email'], data['password'])
        if "success" in result:
            session['user'] = result['user']
            return redirect(url_for('dashboard'))
        return render_template('login.html', error=result['error'])
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    # Refresh user data from DB
    factories = get_factories()
    current_user = next((f for f in factories if f['factory_id'] == session['user']['factory_id']), session['user'])
    session['user'] = current_user # Update session
    
    ai_suggestions = get_ai_suggestions(current_user['carbon_produced'])
    
    return render_template('dashboard.html', user=current_user, ai_suggestions=ai_suggestions)

@app.route('/carbon_input', methods=['GET', 'POST'])
def carbon_input():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        amount = float(request.form['carbon_amount'])
        update_carbon_produced(session['user']['factory_id'], amount)
        return redirect(url_for('dashboard'))
        
    return render_template('carbon_input.html')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        seller_id = request.form['seller_id']
        quantity = float(request.form['quantity'])
        result = buy_carbon(session['user']['factory_id'], seller_id, quantity)
        if "error" in result:
            return render_template('buy_page.html', sellers=get_sellers(), error=result['error'])
        return redirect(url_for('dashboard'))

    return render_template('buy_page.html', sellers=get_sellers())

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        quantity = float(request.form['quantity'])
        price = float(request.form['price'])
        result = set_selling_info(session['user']['factory_id'], quantity, price)
        if "error" in result:
             return render_template('sell_page.html', error=result['error'])
        return redirect(url_for('dashboard'))

    return render_template('sell_page.html')

@app.route('/history')
def history():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    all_tx = get_transactions()
    user_id = session['user']['factory_id']
    user_tx = [t for t in all_tx if t['buyer_id'] == user_id or t['seller_id'] == user_id]
    
    return render_template('history.html', transactions=user_tx)

@app.route('/admin')
def admin():
    # In a real app, check for admin role. Here we just show it.
    factories = get_factories()
    transactions = get_transactions()
    summary = get_admin_summary(factories, transactions)
    return render_template('admin_dashboard.html', factories=factories, transactions=transactions, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
