# Weather CLI App 🌤️

A lightweight, interactive command-line interface (CLI) application built in Python that fetches and displays current weather data for any city using the OpenWeatherMap API.

---

## Features

- **Interactive Shell**: Type a city name to get instant weather data, and type `exit` or `quit` to close the application.
- **Detailed Weather Reports**: Displays temperature, feels-like temperature, humidity, wind speed (converted to km/h), and description of conditions.
- **Zero Third-Party Dependencies**: Built entirely using Python's standard library (`urllib` and `json`). No `pip install` required!

---

## Project Structure

```
Weather App/
├── weather_app.py   # CLI Weather application
├── requirements.txt # External dependencies (empty)
└── README.md        # Project documentation (this file)
```

---

## Setup & Running

### 1. Prerequisites
- Python 3.x
- An API key from [OpenWeatherMap](https://openweathermap.org/api)

### 2. Configure the API Key
Open [weather_app.py](file:///c:/Users/avani/OneDrive/Desktop/CODING/Weather%20App/weather_app.py) in your editor and paste your OpenWeather API key:
```python
API_KEY = "your_api_key_here"
```

### 3. Run the App
Start the application from your terminal:
```bash
python weather_app.py
```
