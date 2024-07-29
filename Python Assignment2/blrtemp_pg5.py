weather_data = [
    {'date': '2024-07-20', 'max_temp': 30, 'min_temp': 20, 'humidity': 70},
    {'date': '2024-07-21', 'max_temp': 32, 'min_temp': 21, 'humidity': 65},
    {'date': '2024-07-22', 'max_temp': 33, 'min_temp': 22, 'humidity': 60},
    {'date': '2024-07-23', 'max_temp': 31, 'min_temp': 23, 'humidity': 68},
    {'date': '2024-07-24', 'max_temp': 29, 'min_temp': 20, 'humidity': 75},
    {'date': '2024-07-25', 'max_temp': 28, 'min_temp': 19, 'humidity': 80},
    {'date': '2024-07-26', 'max_temp': 30, 'min_temp': 21, 'humidity': 72},
]

def average_temperatures(data):
    """Calculates the average maximum and minimum temperatures."""
    total_max_temp = sum(day['max_temp'] for day in data)
    total_min_temp = sum(day['min_temp'] for day in data)
    avg_max_temp = total_max_temp / len(data)
    avg_min_temp = total_min_temp / len(data)
    return avg_max_temp, avg_min_temp

def average_humidity(data):
    """Calculates the average humidity."""
    total_humidity = sum(day['humidity'] for day in data)
    avg_humidity = total_humidity / len(data)
    return avg_humidity

def main():
    avg_max_temp, avg_min_temp = average_temperatures(weather_data)
    print(f"Average Maximum Temperature: {avg_max_temp:.2f}°C")
    print(f"Average Minimum Temperature: {avg_min_temp:.2f}°C")
    
    avg_humidity = average_humidity(weather_data)
    print(f"Average Humidity: {avg_humidity:.2f}%")

if __name__ == "__main__":
    main()
