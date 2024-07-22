
# Weather App

A simple weather application built with Python to fetch real-time weather data using the OpenWeatherMap API and display it using a Tkinter-based GUI.

## Features

- Fetches current weather data for a given city.
- Displays temperature, humidity, and weather description.
- Simple and user-friendly graphical interface.
- Handles user input and displays relevant error messages.
![image](https://github.com/user-attachments/assets/e3dd3b05-5a71-4248-8af6-deb607127b76)
![image](https://github.com/user-attachments/assets/0188bbdc-c78a-4bcf-8301-5f54dd47e31b)


## Prerequisites

- Python 3.x
- OpenWeatherMap API Key

## Installation

1. Clone the repository or download the `weather_app.py` file.
2. Install the required dependencies using pip:
   ```sh
   pip install requests
   ```

## Usage

1. Register at [OpenWeatherMap](https://openweathermap.org/) and obtain your API key.
2. Open the `weather_app.py` file in a text editor and replace `'your_api_key_here'` with your actual API key.
3. Run the application:
   ```sh
   python weather_app.py
   ```

## Code Overview

### Fetching Weather Data

The function `get_weather(city_name, api_key)` uses the `requests` library to fetch weather data from the OpenWeatherMap API.

```python
import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q=${*city_name*}&appid=${*api_key*}&units=metric"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()
```

### GUI with Tkinter

The GUI is created using the Tkinter library. The main components include an input field for the city name, a button to trigger the weather fetch, and labels to display the results.

```python
import tkinter as tk
from tkinter import messagebox

def show_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    api_key = 'your_api_key_here'  # Replace with your actual API key
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
```

## License
This project is licensed under the MIT License.

