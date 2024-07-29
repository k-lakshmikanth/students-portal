from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('home.html', logged_in=current_user.is_authenticated)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', logged_in=current_user.is_authenticated)

@app.route('/academics')
@login_required
def academics():
    return render_template('academics.html', logged_in=current_user.is_authenticated)

@app.route('/courses')
@login_required
def courses():
    courses_list = ['Course 1', 'Course 2', 'Course 3']
    return render_template('courses.html', courses=courses_list, logged_in=current_user.is_authenticated)

@app.route('/updates')
@login_required
def updates():
    updates_list = ['Update 1', 'Update 2', 'Update 3']
    return render_template('updates.html', updates=updates_list, logged_in=current_user.is_authenticated)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', logged_in=current_user.is_authenticated)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User(user_id)
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
