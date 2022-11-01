from flask import Flask,request,abort,session,render_template

from flask_bcrypt import Bcrypt
from config import ApplicationConfig
from flask.json import jsonify


from mailer import emailer
from cryptor import hasher
app = Flask(__name__)
app.config.from_object(ApplicationConfig)


bcrypt=Bcrypt(app)




@app.route("/")
def index():
    return render_template("index.html")



@app.route("/register",methods=["POST","GET"])
def registrationpreotp():

    email=request.form["usersignupemail"]
    name=request.form["usersignupname"]
    password=request.form["usersignuppassword"]




if __name__=="__main__":
    app.run(debug=True)
