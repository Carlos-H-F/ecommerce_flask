from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)



@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/sobre')
def page_home():
    return render_template("sobre.html")
