# Weather_App | Using WeatherAPI


This is a simple weather application built using Tkinter, which provides weather information for a given city. It utilizes the OpenWeatherMap API to fetch weather data.

### Prerequisites

To run this application, you need to have Python installed on your system. Additionally, the following Python packages are required:
- `tkinter`: To create the GUI for the weather app.
- `requests`: To make HTTP requests to the OpenWeatherMap API.
- `time`: To convert timestamps to readable time format.

You can install the required packages using the following command:

```
pip install requests
```

### Usage

1. Clone this repository or download the `weather_app.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `weather_app.py` file is located.

3. Run the following command to start the application:

```
python weather_app.py
```

4. The Weather App window will open. Enter the name of a city in the text entry field and press Enter or click the "Get Weather" button.

5. The application will fetch weather data from the OpenWeatherMap API and display it on the window. The displayed information includes the weather condition, temperature, minimum temperature, maximum temperature, pressure, humidity, wind speed, sunrise time, and sunset time.

6. You can enter a different city name and press Enter or click the button again to fetch weather information for that city.
![image](https://github.com/sriharsha8991/Weather_app/assets/91383946/66a23b4c-8563-40a6-9829-39513b62e303)


7. Close the application window to exit the Weather App.

### Customization

You can customize the appearance of the application by modifying the code in the `weather_app.py` file. You can change the font styles, colors, window size, or add additional elements as per your preference.

Note: Ensure that you have a valid API key from OpenWeatherMap. You can sign up for a free API key at https://openweathermap.org/api and replace the `API_KEY` variable in the `getWeather` function with your own API key.

### License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use it for personal or commercial projects.

### Acknowledgements

- This application was created as a learning project and utilizes the OpenWeatherMap API.
- Thanks to the developers of Tkinter, requests, and time modules for their contributions.
