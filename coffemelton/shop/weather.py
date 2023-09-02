import requests

API_KEY = '57ed3a2ad0d9783da38653dcbd2e9ba4'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',  # Use Celsius for temperature
    }

    response = requests.get(BASE_URL, params=params)
    print(response.url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

def get_weather_with_suggestions(city_name):
    data = get_weather(city_name)

    if data:
        temperature = data['main']['temp']
        suggestions = []

        if 15 <= temperature <= 40:
            suggestions = ['Vein']
        elif 0<= temperature <= 15:
            suggestions = ['Kohv']
        else:
            suggestions = ['Tee']
        # You can add more temperature ranges and corresponding product suggestions

        data['suggestions'] = suggestions

    return data



