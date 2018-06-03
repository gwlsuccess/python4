from flask import Flask,session
from flask_script import Manager
from config import Config
from flask_migrate import Migrate,MigrateCommand
from flask_session import Session
from flask_wtf import CSRFProtect
app = Flask(__name__)
Session(app)
db =Migrate(app)
CSRFProtect(app)
manager =Manager(app)
manager.add_command('db',MigrateCommand)
app.config.from_object(Config)
@app.route('/')
def index():
    session['name']='2022'
    return 'index'

if __name__ == '__main__':
    manager.run()