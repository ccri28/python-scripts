import requests

def get_weather(location):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for imperial units
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return f"Weather in {location}: {weather}, Temperature: {temperature}°C, Humidity: {humidity}%"
    else:
        return "Failed to retrieve weather information."

# Example usage
location = "New York"
weather_info = get_weather(location)
print(weather_info)