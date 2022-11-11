from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

""" @app.route("/favicon.png")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'coffee.ico', mimetype="image/coffee.ico")
 """