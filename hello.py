from flask import Flask
from .import app

app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello, world!'

