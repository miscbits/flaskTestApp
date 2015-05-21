import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/page/')
def page(): 
	return 'This is a second page'
	
if __name__ == '__main__':
    app.run(host='0.0.0.0')
