from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)