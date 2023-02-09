from flask import Flask, jsonify
import requests

zipcodes = {
    "SanFrancisco": "94107",
    "NewYork": "10007",
    "Chicago": "60606",
    "Seattle": "98101",
    "Boston": "02108",
    "LosAngeles": "90001",
}

app = Flask(__name__)

@app.route("/city_to_zip/<city_name>")
def city_to_zip(city_name):
    zipcode = zipcodes.get(city_name)
    if zipcode:
        response = requests.get(f"http://zip2weather:5000/zip_to_weather/{zipcode}")
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Weather service unavailable"}), 503
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
