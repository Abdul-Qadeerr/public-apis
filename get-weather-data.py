import requests
import tkinter as tk
from tkinter import messagebox

# API Config
API_Key = "0c7435b4826bd2ca27521cb85ff4c829"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Function to get weather
def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return
    
    url = f"{BASE_URL}q={city_name}&appid={API_Key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        
        result_label.config(
            text=f"Weather: {weather}\nTemperature: {temp}°C\nFeels Like: {feels_like}°C"
        )
    else:
        messagebox.showerror("Error", "City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.resizable(False, False)

# Widgets
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

get_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
