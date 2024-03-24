from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/recipes")
def recipes():
    return render_template('recipes.html', title='recipes')

if __name__ == '__main__':
    app.run(debug=True)
