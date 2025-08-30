# Using csv lib
# import csv
#
# with open('weather_data.csv', newline="") as file:
#     data = csv.reader(file)
#     weather_data = list(data)
#
# weather_data.pop(0)
# print(weather_data)
#
# temperatures = []
#
# for i in weather_data:
#     temp = int(i[1])
#     temperatures.append(temp)

# for i in weather_data:
#     if i[1] == "temp":
#         continue
#     temp = int(i[1])
#     temperatures.append(temp)

# print(temperatures)
# --------------------------------------------

# Using Pandas
import pandas

weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data)

# weather_data_dict = weather_data.to_dict()
# print(weather_data_dict)
#
# temp_list = weather_data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(f"{average_temp = }")
#
# average_temp_by_mean = weather_data["temp"].mean()
# print(f"{average_temp_by_mean = }")
#
# max_temp_value = weather_data["temp"].max()
# print(f"{max_temp_value = }")
#
# print(weather_data["condition"])
# print(weather_data.day)

# Get a row where the day equal to Monday
# result_by_day = weather_data[weather_data.day == "Monday"]
# print(result_by_day)

# Get a row where the temperature equal to max value
# result_by_max_temp = weather_data[weather_data.temp == max_temp_value]
# print(result_by_max_temp)

# Get value from the needed column after sorted by the day
# monday = weather_data[weather_data.day == "Monday"]
# print(monday.condition)

# Convert monday Celsius temp to Fahrenheit
# monday_temp = int(monday.temp.iloc[0])
# print(monday_temp)
# to_fahrenheit = (monday_temp * 1.8) + 32
# print(to_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

# Saving to the csv file
path = "new_file.csv"
data.to_csv(path)