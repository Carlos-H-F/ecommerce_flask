from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()
app = Flask(__name__)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

import routes
