# -*- coding: utf-8 -*-
"""
Created on Sat Jun 3 21:06:02 2023
@author: sriharsha
"""

import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f167c137a5ff250708425aaf394423c9"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = (
        "\n"
        + "Min Temp: "
        + str(min_temp)
        + "°C"
        + "\n"
        + "Max Temp: "
        + str(max_temp)
        + "°C"
        + "\n"
        + "Pressure: "
        + str(pressure)
        + "\n"
        + "Humidity: "
        + str(humidity)
        + "\n"
        + "Wind Speed: "
        + str(wind)
        + "\n"
        + "Sunrise: "
        + sunrise
        + "\n"
        + "Sunset: "
        + sunset
    )
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
heading_font = ("poppins", 25)  # Define the font for the heading

heading_label = tk.Label(canvas, text="Weather App", font=heading_font)
heading_label.pack(pady=20)  # Add some padding between the heading and other elements


canvas.configure(bg="#e4f0f7")  # Set background color

t = ("poppins", 35, "bold")
f = ("poppins", 15, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t, bg="#c4e5e2", fg="#323232")
label1.pack()

label2 = tk.Label(canvas, font=f, bg="#c4e5e2", fg="#323232")
label2.pack()

canvas.mainloop()
