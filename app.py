from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', logged_in=False)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', logged_in=False)

@app.route('/academics')
def academics():
    return render_template('academics.html', logged_in=False)

@app.route('/courses')
def courses():
    return render_template('courses.html', logged_in=False)

@app.route('/grades')
def grades():
    return render_template('grades.html', logged_in=False)

@app.route('/messages')
def messages():
    return render_template('messages.html', logged_in=False)

@app.route('/events')
def events():
    return render_template('events.html', logged_in=False)

@app.route('/profile')
def profile():
    return render_template('profile.html', logged_in=True)

@app.route('/login')
def login():
    return render_template('login.html', logged_in=False)

if __name__ == '__main__':
    app.run(debug=True)
