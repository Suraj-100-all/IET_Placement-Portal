from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
