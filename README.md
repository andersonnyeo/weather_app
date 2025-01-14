# Weather App

## Overview
The Weather App is a Python-based application that retrieves and displays real-time weather information for a given location using the OpenWeatherMap API. Users can input a city name to get details like the current temperature, weather description, and more.

---

## Features
- Fetch real-time weather data for any city worldwide.
- Display temperature in Celsius (or Fahrenheit, with minor modifications).
- Provide a weather description (e.g., clear sky, rain).
- Error handling for invalid city names or connection issues.

---

## Prerequisites

1. **Install Python**  
   Ensure you have Python 3.6 or later installed. You can download it from [python.org](https://www.python.org/).

2. **Install Required Libraries**  
   The application uses the following Python libraries:
   - `requests` for making HTTP requests.
   - `tkinter` (optional) for creating the GUI.

   To install `requests`, run the following command:
   ```bash
   pip install requests