#!/usr/bin/python
from flask import Flask
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This doucument carries a cookies!</h1>')
    response.set_cookie('ansewe','42')
    return response
#    return '<h1>Hello World!</h1>'
@app.route('/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
