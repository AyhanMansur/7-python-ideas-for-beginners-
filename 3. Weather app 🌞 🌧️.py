# weather_app.py
import requests
import sys

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"\n🌡️  Temperature: {temp}°C")
        print(f"🌤️  Condition: {desc.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
    else:
        print(f"Error: Could not fetch weather data for '{city}'. Status Code: {response.status_code}")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()