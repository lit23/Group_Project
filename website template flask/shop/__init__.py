from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
    app.config['SECRET_KEY'] = '<PLACE-YOUR-SECRET-KEY-HERE>'

#SPECIFY YOUR MYSQL CREDENTIALS:
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://USERNAME:MYSQL_PASSWORD@csmysql.cs.cf.ac.uk:3306/USERNAME'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from shop import routes
