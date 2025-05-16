import requests
from Hydra import config


def fetch_weather(city):
    """
    Fetch weather from WeatherAPI.com
    :param city: City name (string)
    :return: Weather details string
    """
    api_key = config.weather_api_key

    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}"

    response = requests.get(complete_url)
    data = response.json()

    if "error" not in data:
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        pressure = data["current"]["pressure_mb"]
        wind_kph = data["current"]["wind_kph"]

        final_response = f"""
        The weather in {location}, {region}, {country} is currently {condition},
        with a temperature of {temp_c}°C, 
        atmospheric pressure of {pressure} mb,
        humidity at {humidity}%,
        and wind speed of {wind_kph} kph.
        """

        return final_response.strip()
    else:
        return "Sorry Sir, I couldn't find the city in my database. Please try again."
