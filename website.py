from flask import Flask, render_template, url_for, request
import requests
from bs4 import BeautifulSoup
import cssutils


app = Flask(__name__)
def getRecipes(ingredients):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients":ingredients,"number":"6","ignorePantry":"true","ranking":"1"}

    headers = {
        "X-RapidAPI-Key": "0bf75c5ca9msh736ae810a3ac99bp19f126jsn4cc3dd24ab0c",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    array = response.json()
    final = []
    for x in array:
        final.append([x['title'], x['image']])
    return final


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    ingredients = request.form['Ingredients']
    recipes = getRecipes(ingredients)
    print(recipes)
    html = ''
    with open('templates/recipes.html') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    recipe1 = soup.find('span', class_='recipes-text1')
    recipe1.string = recipes[0][0]
    
    recipe2 = soup.find('h1', class_='recipes-text3')
    recipe2.string = recipes[1][0]

    recipe3 = soup.find('h1', class_='recipes-text4')
    recipe3.string = recipes[2][0]

    recipe4 = soup.find('h1', class_='recipes-text5')
    recipe4.string = recipes[3][0]

    recipe5 = soup.find('h1', class_='recipes-text6')
    recipe5.string = recipes[4][0]

    recipe6 = soup.find('h1', class_='recipes-text7')
    recipe6.string = recipes[5][0]

    htmlcontent = str(soup)
    with open('templates/recipes.html', 'w') as f:
        f.write(htmlcontent)

    cssText = ''
    index = 0
    with open('static/styles/recipes.css', 'r') as f:
        line = f.readline()
        while(line):
            if 'background-image' in line:
                cssText += "\n" + '  background-image: url("'  + recipes[index][1]+ '");'
                index+=1
            else:
                cssText += "\n" + line
            line = f.readline()

    # Write the updated CSS back to the file
    with open("static/styles/recipes.css", "w") as f:
        f.write(cssText)

    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)
