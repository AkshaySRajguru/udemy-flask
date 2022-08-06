from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"message": "Hello World!"}

@app.route("/home")
def get_home():
    return render_template("index.html", name="Akshay", template_name = "Taa Daa !")

@app.route("/second")
def get_second():
    return render_template("second.html")
