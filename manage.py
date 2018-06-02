from flask import Flask
from flask_script import Manager
from config import Config

app = Flask(__name__)
manager =Manager(app)
app.config.from_object(Config)
@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()