import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q=${*city_name*}&appid=${*api_key*}&units=metric"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def show_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    api_key = 'API_KEY'  # Replace with your actual API key
    weather_data = get_weather(city_name, api_key)
    
    if weather_data.get('cod') != 200:
        messagebox.showerror("API Error", weather_data.get('message', 'Error fetching weather data'))
        return

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")

# Setting up the GUI
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=show_weather)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
