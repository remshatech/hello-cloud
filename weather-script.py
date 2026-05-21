# weather-script.py
# Fetches weather for multiple cities and saves a report
# Uses: lists, dictionaries, file handling, APIs
# Day 4 — 30-day cloud engineering program

import requests
from datetime import datetime


def get_weather(city):
    """
    Fetches weather for a city using the free wttr.in API.
    Returns a dictionary with weather data, or None if it fails.
    """
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=5)   # timeout=5 means give up after 5 seconds

        # raise_for_status() throws an error if status code is 4xx or 5xx
        response.raise_for_status()

        data = response.json()
        current = data["current_condition"][0]

        # Build and return a clean dictionary
        return {
            "city":        city.title(),
            "temp_f":      current["temp_F"],
            "temp_c":      current["temp_C"],
            "feels_like":  current["FeelsLikeF"],
            "humidity":    current["humidity"],
            "wind_mph":    current["windspeedMiles"],
            "condition":   current["weatherDesc"][0]["value"],
            "fetched_at":  datetime.now().strftime("%Y-%m-%d %H:%M")
        }

    except requests.exceptions.Timeout:
        print(f"  Timeout: {city} took too long to respond")
        return None
    except requests.exceptions.ConnectionError:
        print(f"  Connection error: check your internet")
        return None
    except Exception as e:
        print(f"  Error fetching {city}: {e}")
        return None


def print_weather(weather):
    """Prints a formatted weather summary to the screen."""
    print(f"\n{'=' * 35}")
    print(f"  {weather['city']}")
    print(f"{'=' * 35}")
    print(f"  Temp:      {weather['temp_f']}°F / {weather['temp_c']}°C")
    print(f"  Feels like:{weather['feels_like']}°F")
    print(f"  Humidity:  {weather['humidity']}%")
    print(f"  Wind:      {weather['wind_mph']} mph")
    print(f"  Condition: {weather['condition']}")
    print(f"  Fetched:   {weather['fetched_at']}")


def save_report(weather_list, filename="weather-report.txt"):
    """
    Saves all weather data to a text file.
    weather_list is a list of dictionaries.
    """
    with open(filename, "w") as f:
        f.write("Weather Report\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("=" * 35 + "\n\n")

        for weather in weather_list:
            f.write(f"City:      {weather['city']}\n")
            f.write(f"Temp:      {weather['temp_f']}°F / {weather['temp_c']}°C\n")
            f.write(f"Humidity:  {weather['humidity']}%\n")
            f.write(f"Condition: {weather['condition']}\n")
            f.write("\n")

    print(f"\nReport saved to: {filename}")


def find_hottest(weather_list):
    """Returns the city with the highest temperature."""
    # int() converts the string "89" to the number 89 so we can compare
    hottest = max(weather_list, key=lambda w: int(w["temp_f"]))
    return hottest


def find_most_humid(weather_list):
    """Returns the city with the highest humidity."""
    most_humid = max(weather_list, key=lambda w: int(w["humidity"]))
    return most_humid


# ================================================
# MAIN PROGRAM
# ================================================

# List of cities to check
cities = ["Orlando", "New York", "London", "Tokyo", "Sydney"]

print("Fetching weather data...")
print("-" * 35)

# Fetch weather for each city
# Build a list of dictionaries — one per city
results = []

for city in cities:
    print(f"  Fetching: {city}...")
    weather = get_weather(city)

    if weather is not None:       # only add if fetch succeeded
        results.append(weather)
        print_weather(weather)

# Summary section
if results:
    print(f"\n{'=' * 35}")
    print("  SUMMARY")
    print(f"{'=' * 35}")
    print(f"  Cities fetched: {len(results)}")

    hottest = find_hottest(results)
    humid   = find_most_humid(results)

    print(f"  Hottest city:   {hottest['city']} ({hottest['temp_f']}°F)")
    print(f"  Most humid:     {humid['city']} ({humid['humidity']}%)")

    # Save the report
    save_report(results)