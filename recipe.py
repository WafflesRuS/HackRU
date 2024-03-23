from flask import Flask, render_template, url_for

app = Flask(__name__)

recipes = [
    {

    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')