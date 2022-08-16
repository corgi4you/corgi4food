import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/foods/random", methods=['GET'])
def foods_random():
    random_meal = requests.get("http://www.themealdb.com/api/json/v1/1/random.php")
    try:
        data = json.loads(random_meal.text)
        res = {
            "data": data["meals"][0],
        }
        return res, 200
    except:
        return "Server error", 500

@app.route("/etc", methods=['POST'])
def etc():
    item = request.get_json()
    return item['item'], 200

if __name__ == "__main__":
    app.run(debug=True)
