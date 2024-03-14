from flask import Flask, render_template, request, url_for, redirect, session, g
from markupsafe import escape
from datetime import timedelta
import sqlite3 as sql
from pathlib import Path
#from hashlib import encode, hexdigest
#hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()

# CONSTANT
DATABASE_PATH = 'projet.db'
SCRIPTSQL_PATH = 'script.sql'

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour le chiffrement du cookie de session
app.permanent_session_lifetime = timedelta(hours=2)  # La duree de vie de la session 2 heures

# =========== INIT DB  ==========
db_path = Path(DATABASE_PATH)
if not db_path.exists():
        script_path = Path(SCRIPTSQL_PATH)
        
        with script_path.open() as script_file:
            script = script_file.read()
        
        con = sql.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.executescript(script)
        con.commit()
        con.close()
else:
    sql.connect(DATABASE_PATH)

# Page Index =============
@app.route('/')
def displayIndexPage():
    return render_template('index.html')

# Page de connexion
@app.route('/login')
def displayLoginPage():
    if session.get('logged_in'):
        return redirect(url_for('displayApplication'))
    else:
        isError = request.args.get('failToLog')
        return render_template('login.html', failToLog=isError)

@app.route('/register')
def displayResgisterPage():
    if session.get('logged_in'):
        return redirect(url_for('displayApplication'))
    else:
        msg = request.args.get('errorMsg')
        return render_template('register.html', errorMsg=msg)

@app.route('/register/new',methods = ['POST'])
def registerToApplication():
    newUserName = request.form['username']
    newUserPass = request.form['password']
    newUserPassConf = request.form['confirm_password']
    newUserNick = request.form['nickname']
       
    if not(newUserPass == newUserPassConf):
        return redirect(url_for('displayResgisterPage',errorMsg="Les mots de passe ne sont pas identique"))
    elif getUserPassword(newUserName,newUserPass):
        return redirect(url_for('displayResgisterPage',errorMsg="Ce nom d'utilisateur est déja utilisé."))
    elif newUserNick == "":
        newUserNick = newUserName
            
    addUserPassword(newUserName,newUserPass,newUserNick)
    return redirect(url_for('displayLoginPage'))
            
            

# Connexion
@app.route('/connect', methods=['POST'])
def connectToApplication():
    user = request.form["username"]
    password = request.form["password"]

    userData = getUserPassword(user,password)
    if userData:
         isUserAllowed = True
    else:
        isUserAllowed = False
    
    if isUserAllowed:
        session['logged_in'] = True
        session['username'] = userData[3]
        
        return redirect(url_for('displayApplication'))
    else:
        return redirect(url_for('displayLoginPage', failToLog=True))


# Page de l'application
@app.route('/monagenda')
def displayApplication():
    if session.get('logged_in'):
        nick = session.get('username')
        return render_template('appli.html',nickname=nick)
    else:
        return redirect(url_for('displayLoginPage'))
    
# Deconnexion
@app.route('/monagenda/addevent')
def displayApplicationNewEvent():
    if session.get('logged_in'):
        nick = session.get('username')
        return render_template('new_event.html',nickname=nick)
    else:
        return redirect(url_for('displayLoginPage'))

@app.route('/disconnect')
def disconnectFromApplication():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('displayLoginPage'))

# ================= DATABASE ==================
def getUserPassword(username,password):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    reponse = cur.execute("SELECT * FROM user WHERE username like ? and passwordUser like ?;",[username,password]).fetchone()
    con.close()
    
    return reponse

def addUserPassword(username,password,nickname):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    print('username,password,nickname')
    print(username,password,nickname)
    reponse = cur.execute('INSERT INTO user (username, passwordUser, nickname, type_user) VALUES (?, ?, ?, 1);',[username,password,nickname]).fetchone()
    con.commit()
    con.close()
    
    return reponse


