import requests  


API_KEY = "e760fe4ea56375f8274bd2549050e3e2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 City: {city}")
        print(f"🌤️ Weather: {weather}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")

    else:
        print("❌ City not found. Please try again.")


city_name = input("Enter city name: ")
get_weather(city_name)
