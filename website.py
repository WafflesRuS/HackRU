from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"apples,flour,sugar","number":"5","ignorePantry":"true","ranking":"2"}

headers = {
    "X-RapidAPI-Key": "2664f58407msha99b2252514da90p12ac7bjsnfcace937a84b",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
recipes = response.json()

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)