import urllib.request
import urllib.error
import urllib.parse
import json

API_KEY = "c3703c3c361e8b48255d07109b4c3e8c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    params = urllib.parse.urlencode({"q": city_name, "appid": API_KEY, "units": "metric"})
    full_url = BASE_URL + "?" + params

    try:
        response = urllib.request.urlopen(full_url)
        raw_data = response.read().decode("utf-8")
        weather_data = json.loads(raw_data)
        return weather_data

    except urllib.error.HTTPError as http_error:
        if http_error.code == 404:
            print("\n  [!] City not found. Please check the spelling and try again.")
        elif http_error.code == 401:
            print("\n  [!] Invalid API Key. Please check your API key in the code.")
        else:
            print(f"\n  [!] HTTP Error occurred: {http_error.code} - {http_error.reason}")
        return None

    except urllib.error.URLError as url_error:
        print("\n  [!] Network error. Please check your internet connection.")
        print(f"      Details: {url_error.reason}")
        return None

    except Exception as general_error:
        print(f"\n  [!] Something went wrong: {general_error}")
        return None


def display_weather(weather_data):
    city_name = weather_data["name"]
    country_code = weather_data["sys"]["country"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    wind_speed_kmph = round(wind_speed * 3.6, 2)

    print("\n" + "=" * 45)
    print(f"  Weather Report: {city_name}, {country_code}")
    print("=" * 45)
    print(f"  Temperature   : {temperature}°C  (Feels like {feels_like}°C)")
    print(f"  Condition     : {condition.title()}")
    print(f"  Humidity      : {humidity}%")
    print(f"  Wind Speed    : {wind_speed_kmph} km/h")
    print("=" * 45)


def main():
    print("\n" + "*" * 45)
    print("*       WEATHER APP - OpenWeatherMap        *")
    print("*" * 45)
    print("  Type a city name to get current weather.")
    print("  Type 'exit' or 'quit' to stop the program.")

    while True:
        print()

        city_input = input("  Enter city name: ").strip()

        if city_input.lower() == "exit" or city_input.lower() == "quit":
            print("\n  Thank you for using Weather App. Goodbye!\n")
            break

        if city_input == "":
            print("  [!] City name cannot be empty. Please try again.")
            continue

        weather_data = get_weather(city_input)

        if weather_data is not None:
            display_weather(weather_data)


if __name__ == "__main__":
    main()
