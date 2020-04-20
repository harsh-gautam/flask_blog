from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '23jbhbh21h1gvbdv12g3vjdgva7atd12hj8asd'

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)