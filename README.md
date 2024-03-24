# HackRU
## Inspiration
Our inspiration for this project was when we realized that many people do not know what to make with the things they have at home, making them tend to purchase food from outside. As a result we decided to create this website to help these people, and other people figure out what food to make based on the ingredients they have at home in their pantry.

## What it does
This function takes a list of comma separated ingredients, and returns potential foods that you can make with the ingredients that you have at home.

## How we built it
We built this website by using the spoonacular API to pull data that would give us specific recipes that matched the list of ingredients given. We then used beautiful soup with flask to use this data to alter values in our html file that we made for the website. our html and CSS files made up of the design of the website in a different folder.

## Challenges we ran into
Some challenges that we ran into were figuring out how to use the flask as none of us had ever used flask before. It was annoying trying to figure out the specifics of flask, like having a static folder and a templates folder. Another challenge that we ran into was trying to alter the CSS files, as while the HTML file let us use beautiful soup, the CSS file had the same property names for each section we needed to alter, as a result it made it harder to figure out how to update values within this file.

## Accomplishments that we're proud of
Some accomplishments that we are proud of is creating the HTML and CSS, while learning how to implement flask into our code. It was a great accomplishment to successfully integrate flask to our program.

## What we learned
We learned more of the nuances of using HTML while learning how to use flask and beautiful soup to host and alter our HTML file in our website.

## What's next for ReSpicy
We plan to further our project by actually being able to integrate the recipe and highlight specifics, like which ingredients are missing. This would be achieved when somebody clicks on one of the recipes.
