import json
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/foods/random")
def foods_random():
    random_meal = requests.get("http://www.themealdb.com/api/json/v1/1/random.php")
    #try:
    data = json.loads(random_meal.text)
    res = {
        "data": data["meals"][0],
    }
    ingredients = []
    for k, v in res['data'].items():
        if 'Ingredient' in k:
            ingredient = {
                k: v
            }
            ingredients.append(ingredient)
    print(ingredients)
    recipe = {
        "idMeal": res['data']['idMeal'],
        "strArea": res['data']['strArea'],
        "strCategory": res['data']['strCategory'],
        "ingredients": ingredients,
        "strInstructions": res['data']['strInstructions'],
        "strMeal": res['data']['strMeal'],
        "strMealThumb": res['data']['strMealThumb'],
        "strSource": res['data']['strSource'],
        "strYoutube": res['data']['strYoutube']
    }
    return recipe, 200
    #except:
    #    return "a", 500

if __name__ == "__main__":
    app.run(debug=True)
