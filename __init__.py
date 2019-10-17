from flask import Flask, escape, request
from flask import render_template, g, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/panel')
def panel():
    return render_template('panel.html')


@app.route('/login')
def login():
    return render_template('home_login.html')

if __name__ == '__main__':
    app.run(debug=True)