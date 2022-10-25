from flask import Flask,request,abort,session
from models import db,Users,Otp
from flask_bcrypt import Bcrypt
from config import ApplicationConfig
from flask.json import jsonify
import random
from sqlalchemy import *
from mailer import emailer
from cryptor import hasher
app = Flask(__name__)
app.config.from_object(ApplicationConfig)


bcrypt=Bcrypt(app)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/register",methods=["POST"])
def registrationpreotp():

    email=request.json["email"]
    name=request.json["name"]
    password=request.json["password"]

    user_exists=Users.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error":"User already exists"}),409
    otp = random.randrange(100000, 999999)
    emailer(otp,email,name)
    otpstore=Otp(id=random.randrange(10000,99999),email=email,generated_otp=otp)
    db.session.add(otpstore)
    db.session.commit()

    otpid=Otp.query.filter_by(email=email).order_by(Otp.ctime.desc()).first()

    print("podaaaa")
    print(otpid.id)

    return jsonify({
        "id":hasher(otpid.id),
        "otp":otp,
        "email":email
    })

@app.route("/registerform/<id>",methods=["POST","GET"])
def register_user(id):

    email=request.json["email"]
    name=request.json["name"]
    password=request.json["password"]
    otp=request.json["otp"]
    user_exists=Users.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error":"User already exists"}),409
    otpcheck=Users.query.filter_by(or_(id=id,otp=otp))
    hashed=bcrypt.generate_password_hash(password)
    newuser=Users(email=email,name=name,password=hashed)
    db.session.add(newuser)
    db.session.commit()
    return jsonify({
        "id":newuser.id,
        "email":newuser.email

    })



@app.route("/login",methods=["POST"])
def login_user():
    email=request.json["email"]
    password= request.json["password"]
    user=Users.query.filter_by(email=email).first()
    if user is None:
        return jsonify({
            "error":"Unauthorized access"
        }),401
    if bcrypt.check_password_hash(user.password,password):
        return jsonify({
            "error": "Password do not match"
        }), 401
    return jsonify({
        "id": user.id,
        "email": user.email
    })

if __name__=="__main__":
    app.run(debug=True)
