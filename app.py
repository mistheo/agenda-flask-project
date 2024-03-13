from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from markupsafe import escape

app = Flask(__name__)

@app.get('/')
def displayIndexPage():
    return render_template('index.html')

@app.get('/login')
def displayLoginPage():
    isError = bool(request.args.get('failToLog'))
    if (isError):
        return render_template('login.html',failToLog=True)
    else:
        return render_template('login.html',failToLog=False)


@app.post('/connect')    
def connectToApplication():
    user = request.form["username"]
    password = request.form["password"]
    
    print(f"'{user}' : '{password}'")
    
    if(user == "test" and password == "123"):
        return redirect(url_for('loadToApplication'))
    else:
        return redirect(url_for('displayLoginPage',failToLog=True))
   

@app.get('/application') 
def loadToApplication():
   return render_template('appli.html')