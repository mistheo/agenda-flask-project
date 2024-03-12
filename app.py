from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/login')
def login():
        return render_template('login.html')
