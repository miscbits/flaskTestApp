import os

from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0')
