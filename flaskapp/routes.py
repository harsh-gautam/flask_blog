from flaskapp import app
from flask import render_template, url_for, flash, redirect
from flaskapp.forms import LoginForm, RegistrationForm
from flaskapp.database import User, Posts

posts = [
    {
        'author':'Harsh Gautam',
        'date':'April 20th 2020',
        'title':'Blog Post 1',
        'content':'This is blog 1'
    },
    {
        'author':'iCeFire',
        'date':'April 21st 2020',
        'title':'Blog Post 2',
        'content':'This is blog 2'
    }
]

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
