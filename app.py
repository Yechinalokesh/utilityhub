from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# In-memory task list for To-Do List
tasks = []

# In-memory user store (for demonstration purposes)
users = []

# Register page route
@app.route('/')
def register():
    return render_template('register.html')

# Login page route
@app.route('/login.html')
def login():
    return render_template('login.html')

# Index page route
@app.route('/index.html')
def index():
    return render_template('index.html')

# BMI Calculator route
@app.route('/bmi_calculator', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    error_message = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height']) / 100  # Convert height to meters
            bmi = round(weight / (height ** 2), 2)
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"
        except (ValueError, ZeroDivisionError):
            error_message = "Invalid input. Please enter valid numbers."
    return render_template('bmi_calculator.html', bmi=bmi, category=category, error_message=error_message)

# Route for To-Do List
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append({'task': task, 'done': False})
    return render_template('todo.html', tasks=tasks)

# Mark task as done
@app.route('/mark_done/<int:task_id>', methods=['GET'])
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('todo'))

# Delete task
@app.route('/delete_task/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('todo'))

# Loan EMI Calculator route
@app.route('/loan_emi_calculator', methods=['GET', 'POST'])
def loan_emi_calculator():
    emi = None
    error_message = None
    if request.method == 'POST':
        try:
            # Get input values from the form
            loan_amount = float(request.form['loan_amount'])
            annual_rate = float(request.form['annual_rate'])
            tenure_years = int(request.form['tenure_years'])

            # Convert annual interest rate to monthly rate
            monthly_rate = annual_rate / (12 * 100)

            # Convert loan tenure to months
            tenure_months = tenure_years * 12

            # EMI Calculation using the formula
            emi = round((loan_amount * monthly_rate * (1 + monthly_rate)**tenure_months) / ((1 + monthly_rate)**tenure_months - 1), 2)

        except ValueError:
            error_message = "Invalid input. Please enter valid numbers."
    return render_template('loan_emi_calculator.html', emi=emi, error_message=error_message)

# Pomodoro Timer route
@app.route('/pomodoro', methods=['GET', 'POST'])
def pomodoro():
    # Example values for the timer and type
    timer = 1500  # 25 minutes in seconds
    timer_type = 'work'  # or 'break'
    work_duration = 1500  # 25 minutes in seconds
    break_duration = 300  # 5 minutes in seconds

    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'start':
            # Start the timer
            pass  # You should manage timer state updates here
        
        elif action == 'pause':
            # Pause the timer
            pass
        
        elif action == 'reset':
            # Reset the timer
            timer = work_duration  # Reset to work time
            timer_type = 'work'

    return render_template('pomodoro.html', timer=timer, timer_type=timer_type, work_duration=work_duration, break_duration=break_duration)

# In-memory grocery shopping list
grocery_list = []

# Route for Grocery Shopping List
@app.route('/grocery', methods=['GET', 'POST'])
def grocery():
    if request.method == 'POST':
        item = request.form['item']
        if item:
            grocery_list.append({'item': item, 'bought': False})
    return render_template('grocery.html', grocery_list=grocery_list)

# Mark item as bought
@app.route('/mark_bought/<int:item_id>', methods=['GET'])
def mark_bought(item_id):
    if 0 <= item_id < len(grocery_list):
        grocery_list[item_id]['bought'] = True
    return redirect(url_for('grocery'))

# Delete item
@app.route('/delete_item/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    if 0 <= item_id < len(grocery_list):
        grocery_list.pop(item_id)
    return redirect(url_for('grocery'))

if __name__ == '__main__':
    app.run(debug=True)
