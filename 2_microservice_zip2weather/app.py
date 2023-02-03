from flask import Flask, jsonify

app = Flask(__name__)

weathers = {
    "94107": {
        "temperature": 72,
        "humidity": 48,
        "wind_speed": 12
    },
    "10007": {
        "temperature": 68,
        "humidity": 52,
        "wind_speed": 14
    },
    "60606": {
        "temperature": 65,
        "humidity": 55,
        "wind_speed": 16
    },
    "98101": {
        "temperature": 70,
        "humidity": 50,
        "wind_speed": 10
    },
    "02108": {
        "temperature": 69,
        "humidity": 51,
        "wind_speed": 11
    },
    "90001": {
        "temperature": 75,
        "humidity": 45,
        "wind_speed": 9
    }
}

@app.route("/zip_to_weather/<zipcode>")
def zip_to_weather(zipcode):
    weather = weathers.get(zipcode, None)
    if weather:
        return jsonify(weather)
    else:
        return jsonify({"error": "Zipcode not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
