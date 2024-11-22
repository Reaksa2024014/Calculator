


 
# import requests
# import matplotlib.pyplot as plt

# def collect_weather_data(city):
#     api_key = "cdecff0c99b1d9ebf848385e585d7640"  # Replace with your OpenWeatherMap API key
#     # Fetch weather data from OpenWeatherMap
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         # Extract daily temperatures for the next 5 days
#         temperatures = []
#         for i in range(5):
#             temperatures.append(data['list'][i * 8]['main']['temp'])  # 8 entries per day, take the first one
            
#         return temperatures
#     else:
#         print("Error fetching data:", response.status_code)
#         return None

# def calculate_average(temperatures):
#     return sum(temperatures) / len(temperatures)

# def find_highest(temperatures):
#     return max(temperatures)

# def find_lowest(temperatures):
#     return min(temperatures)

# def present_results(average, highest, lowest):
#     print("\nWeather Analysis Results:")
#     print(f"Average Temperature: {average:.2f}°C")
#     print(f"Highest Temperature: {highest:.2f}°C")
#     print(f"Lowest Temperature: {lowest:.2f}°C")

# def plot_temperatures_line_chart(temperatures):
#     plt.figure(figsize=(10, 5))
#     plt.plot(temperatures, marker='o', color='b')
#     plt.title('Temperature Data Analysis')
#     plt.xlabel('Days')
#     plt.ylabel('Temperature (°C)')
#     plt.xticks(range(len(temperatures)), [f'Day {i+1}' for i in range(len(temperatures))])
#     plt.grid(True)
#     plt.show()

# def main():
#     city = input("Enter the city name: ")  # User inputs city name
#     temperatures = collect_weather_data(city)
    
#     if temperatures:
#         average = calculate_average(temperatures)
#         highest = find_highest(temperatures)
#         lowest = find_lowest(temperatures)

#         present_results(average, highest, lowest)
#         plot_temperatures_line_chart(temperatures)

# if __name__ == "__main__":
#     main()












# import requests
# import matplotlib.pyplot as plt

# def collect_weather_data(city):
#     api_key = "cdecff0c99b1d9ebf848385e585d7640"  # Replace with your OpenWeatherMap API key
#     # Fetch weather data from OpenWeatherMap
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
        
#         if 'list' in data:
#             # Extract daily temperatures for the next 5 days
#             temperatures = []
#             for i in range(5):
#                 try:
#                     temperatures.append(data['list'][i * 8]['main']['temp'])  # 8 entries per day, take the first one
#                 except IndexError:
#                     print(f"Error: Not enough data available for day {i + 1}")
#                     break
#             return temperatures
#         else:
#             print("Error: Unexpected response structure from the API")
#             return None
#     else:
#         print(f"Error fetching data: {response.status_code}")
#         return None

# def calculate_average(temperatures):
#     return sum(temperatures) / len(temperatures)

# def find_highest(temperatures):
#     return max(temperatures)

# def find_lowest(temperatures):
#     return min(temperatures)

# def present_results(average, highest, lowest):
#     print("\nWeather Analysis Results:")
#     print(f"Average Temperature: {average:.2f}°C")
#     print(f"Highest Temperature: {highest:.2f}°C")
#     print(f"Lowest Temperature: {lowest:.2f}°C")

# def plot_temperatures_line_chart(temperatures):
#     plt.figure(figsize=(10, 5))
#     plt.plot(temperatures, marker='o', color='b')
#     plt.title('Temperature Data Analysis')
#     plt.xlabel('Days')
#     plt.ylabel('Temperature (°C)')
#     plt.xticks(range(len(temperatures)), [f'Day {i+1}' for i in range(len(temperatures))])
#     plt.grid(True)
#     plt.show()

# def main():
#     city = input("Enter the city name: ")  # User inputs city name
#     temperatures = collect_weather_data(city)
    
#     if temperatures:
#         average = calculate_average(temperatures)
#         highest = find_highest(temperatures)
#         lowest = find_lowest(temperatures)

#         present_results(average, highest, lowest)
#         plot_temperatures_line_chart(temperatures)

# if __name__ == "__main__":
#     main()









# import requests
# import matplotlib.pyplot as plt

# def collect_weather_data(city):
#     api_key = "dc0884e71baa845a525e44cc65b275e9"  # Replace with your OpenWeatherMap API key
#     # Construct the API URL for fetching the 5-day weather forecast
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
#     response = requests.get(url) 
    
#     if response.status_code == 200:  
#         data = response.json()  
#         temperatures = []  
        
    
#         for i in range(5):
#             temperatures.append(data['list'][i * 8]['main']['temp']) 
            
#         return temperatures  
#     else:
#         print("Error fetching data:", response.status_code)  
#         return None

# def calculate_average(temperatures):
#     return sum(temperatures) / len(temperatures) 


# def find_highest(temperatures):
#     return max(temperatures)  

# def find_lowest(temperatures):
#     return min(temperatures)  

# def present_results(average, highest, lowest):
#     print("\nWeather Analysis Results:")
#     print(f"Average Temperature: {average:.2f}°C") 
#     print(f"Highest Temperature: {highest:.2f}°C") 
#     print(f"Lowest Temperature: {lowest:.2f}°C")   


# def plot_temperatures_line_chart(temperatures):
#     plt.figure(figsize=(10, 5))  
#     plt.plot(temperatures, marker='o', color='b')  
#     plt.title('Temperature Data Analysis') 
#     plt.xlabel('Days')  
#     plt.ylabel('Temperature (°C)')  
#     plt.xticks(range(len(temperatures)), [f'Day {i+1}' for i in range(len(temperatures))])  
#     plt.grid(True) 
#     plt.show()  

# def main():
#     city = input("Enter the city name: ")  
#     temperatures = collect_weather_data(city)  
#     if temperatures: 
#         average = calculate_average(temperatures)  
#         highest = find_highest(temperatures)  
#         lowest = find_lowest(temperatures)  

#         present_results(average, highest, lowest)
        
#         plot_temperatures_line_chart(temperatures)
#     else:
#         print("Could not retrieve temperature data.") 
# if __name__ == "__main__":
#     main()



 
