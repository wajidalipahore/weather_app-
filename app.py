
import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import ttk

# Function to get weather data
def get_weather():
    city = city_entry.get()
    api_key = "9b58c704ccd7798a9999c35a17a2017e"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},pk&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "200":
            # Get current weather
            current_weather = data["list"][0]
            temp = current_weather["main"]["temp"]
            humidity = current_weather["main"]["humidity"]
            weather = current_weather["weather"][0]["description"]
            wind_speed = current_weather["wind"]["speed"]

            # Display current weather data
            weather_label.config(text=f"Weather: {weather.capitalize()}")
            temp_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
            
            # Get the 5-day forecast
            forecast_text = "5-Day Forecast:\n"
            for i in range(0, 40, 8):  # Each day has 8 records in 3-hour intervals
                day = data["list"][i]
                day_date = day["dt_txt"]
                day_temp = day["main"]["temp"]
                day_weather = day["weather"][0]["description"]
                forecast_text += f"{day_date}: {day_weather.capitalize()} | Temp: {day_temp}°C\n"
            
            forecast_label.config(text=forecast_text)

            # Clear button is enabled after successful fetch
            clear_button.config(state=tk.NORMAL)

        else:
            messagebox.showerror("Error", "City not found. Please try again.")
            clear_fields()

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Error fetching data. Please check your internet connection.")
        clear_fields()

# Function to clear all fields
def clear_fields():
    city_entry.delete(0, tk.END)
    weather_label.config(text="Weather: ")
    temp_label.config(text="Temperature: ")
    humidity_label.config(text="Humidity: ")
    wind_label.config(text="Wind Speed: ")
    forecast_label.config(text="5-Day Forecast: ")

# Create the main window
root = tk.Tk()
root.title("Weather App for Pakistan")
root.geometry("500x600")
root.configure(bg="#e6f7ff")

# Create the UI elements
title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), bg="#e6f7ff")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg="#e6f7ff")
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

# Get Weather Button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white", width=20)
get_weather_button.pack(pady=10)

# Weather Information Labels
weather_label = tk.Label(root, text="Weather: ", font=("Arial", 12), bg="#e6f7ff")
weather_label.pack(pady=5)

temp_label = tk.Label(root, text="Temperature: ", font=("Arial", 12), bg="#e6f7ff")
temp_label.pack(pady=5)

humidity_label = tk.Label(root, text="Humidity: ", font=("Arial", 12), bg="#e6f7ff")
humidity_label.pack(pady=5)

wind_label = tk.Label(root, text="Wind Speed: ", font=("Arial", 12), bg="#e6f7ff")
wind_label.pack(pady=5)

# 5-Day Forecast Label
forecast_label = tk.Label(root, text="5-Day Forecast: ", font=("Arial", 10), bg="#e6f7ff", justify=tk.LEFT)
forecast_label.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_fields, font=("Arial", 12), bg="#FF6347", fg="white", width=20, state=tk.DISABLED)
clear_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
