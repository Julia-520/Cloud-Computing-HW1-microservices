import requests

def get_zipcode(city_name):
    response = requests.get(f"http://localhost:8000/city_to_zip/{city_name}")
    if response.status_code == 200:
        return response.json()["zipcode"]
    else:
        raise Exception("City not found")

def get_weather(zipcode):
    response = requests.get(f"http://localhost:8001/zip_to_weather/{zipcode}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Zipcode not found")

def main():
    city_name = input("Enter city name: ")
    try:
        zipcode = get_zipcode(city_name)
        weather = get_weather(zipcode)
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather['temperature']}")
        print(f"Humidity: {weather['humidity']}")
        print(f"Wind Speed: {weather['wind_speed']}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
