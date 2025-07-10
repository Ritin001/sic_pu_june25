import requests

# Your OpenWeatherMap API key
api_key = "6600d7b9f29122fa587ae27d08e9500c" #'your_api_key'
# City for which you want the weather
city = 'kodaikanal' #'London'

# API endpoint
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    weather_data = response.json()
    
    # Extract and print the relevant information
    print(f"City: {weather_data['name']}")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print(f"Failed to get weather data. Status code: {response.status_code}")