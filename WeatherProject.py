import requests

API_KEY = "31a745caf0ba574639273c13e63507c3"  # Replace with your actual OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extracting useful information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display the data
        print(f"\nWeather in {city_name}:")
        print(f"  Description: {weather}")
        print(f"  Temperature: {temperature}°C (feels like {feels_like}°C)")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except KeyError:
        print("Could not retrieve weather data. Please check the city name.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
