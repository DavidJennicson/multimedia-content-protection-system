from flask import Flask,request,abort,session,render_template
from registration import *
import psycopg2
from fetcher import *
import psycopg2.extras
from flask.json import jsonify
uploadfolder=

from mailer import emailer
from cryptor import hasher
app = Flask(__name__)

conn = psycopg2.connect(dbname="medcrypt", user="postgres", password="Jennicson1", host="localhost")




@app.route("/")
def index():
    return render_template("index.html")



@app.route("/register",methods=["POST","GET"])
def registrationpreotp():

    email=request.form["usersignupemail"]
    name=request.form["usersignupname"]
    password=request.form["usersignuppassword"]
    register(name,email,password)
    return "success"

@app.route("/login",methods=["POST"])
def login():
    return "g"

@app.route("/dashboard",methods=["POST","GET"])
def dashboard():
    filedata=fetcharr()
    return render_template('dashboard.html',filedata=filedata)


@app.route("/files",methods=['POST','GET'])
def fileupload():
    if request.method=="POST":
        f=request.files['fileup']

        return "siuuuu"

if __name__=="__main__":
    app.run(debug=True)
