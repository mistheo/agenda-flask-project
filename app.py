from flask import Flask, render_template, request, url_for, redirect, session
from markupsafe import escape
from datetime import timedelta
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour le chiffrement du cookie de session
app.permanent_session_lifetime = timedelta(hours=2)  # Durée de vie de la session : 2 heures

# Page d'accueil
@app.route('/')
def displayIndexPage():
    return render_template('index.html')

# Page de connexion
@app.route('/login')
def displayLoginPage():
    if session.get('logged_in'):
        return redirect(url_for('loadToApplication'))
    else:
        isError = request.args.get('failToLog')
        return render_template('login.html', failToLog=isError)

# Traitement de la connexion
@app.route('/connect', methods=['POST'])
def connectToApplication():
    user = request.form["username"]
    password = request.form["password"]

    isUserAllowed = isUserPasswordExist(user,password)
    print(f"'{isUserAllowed}'")
    
    if isUserAllowed[0]:
        session['logged_in'] = True
        return redirect(url_for('loadToApplication'))
    else:
        return redirect(url_for('displayLoginPage', failToLog=True))

# Page de l'application
@app.route('/application')
def loadToApplication():
    if session.get('logged_in'):
        return render_template('appli.html')
    else:
        return redirect(url_for('displayLoginPage'))

# Déconnexion
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('displayIndexPage'))



def isUserPasswordExist(username,password):
    con = sql.connect("projet.db")
    cur = con.cursor()
    reponse = cur.execute(f"SELECT * FROM user WHERE username like '{username}' and passwordUser like {password};").fetchone()
    con.close()
    if reponse:
        return True, reponse
    else:
        return False, reponse