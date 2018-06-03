from flask import Flask
from flask_script import Manager
from config import Config
from flask_migrate import Migrate,MigrateCommand
app = Flask(__name__)
db =Migrate(app)
manager =Manager(app)
manager.add_command('db',MigrateCommand)
app.config.from_object(Config)
@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()