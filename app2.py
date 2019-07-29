from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_required, login_user

from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'render_login'
login_manager.login_message = None # Don't set any Flask flash messages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return 'Dashboard'


@app.route('/login', methods=['GET', 'POST'])
def render_login():
    # import os
    # print(os.path.abspath(os.path.dirname(__file__)))
    if current_user.is_authenticated:
        return redirect(url_for('app.dashboard'))

    next = request.args.get('next')

    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested {} {}'.format(form.username.data, form.password.data), 'alert alert-danger alert-dismissible fade show')
        return redirect(next)
    return render_template('login.html', form=form)


@app.route('/login', methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    next = request.args.get('next')
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested {} {}'.format(form.username, form.password))
        return 'success'
    if username == 'ed' and password == '123':
        login_user()
        return redirect(next)
    flash('Incorrect username or password.', 'alert alert-danger alert-dismissible fade show')
    return redirect(next)


if __name__ == '__main__':
    app.run(debug=True)
