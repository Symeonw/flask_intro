from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/roll_dice")
def dice():
    return random.randint(1, 10)
