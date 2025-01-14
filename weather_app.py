import tkinter as tk
from tkinter import messagebox
import requests

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "City name cannot be empty")
        return

    api_key = "6ed7be632fe4eead27f5426634bd0dc4"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            city_name = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            result_label.config(
                text=f"Weather in {city_name}:\nTemperature: {temperature}°C\nDescription: {description.capitalize()}"
            )
        else:
            result_label.config(text="City not found. Please try again.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# GUI setup
app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter City:").pack(pady=10)
city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

fetch_button = tk.Button(app, text="Get Weather", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

app.mainloop()
