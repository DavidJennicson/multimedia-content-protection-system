from flask import Flask,request,abort,session,render_template
from registration import *


from flask.json import jsonify


from mailer import emailer
from cryptor import hasher
app = Flask(__name__)






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
    
if __name__=="__main__":
    app.run(debug=True)
