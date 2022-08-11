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
    data = json.loads(random_meal.text)
    res = {
        "data": data["meals"][0],
    }
    return res, 200

if __name__ == "__main__":
    app.run(debug=True)
