from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html')

def recipe_page():
    return render_template('recipes.html')
