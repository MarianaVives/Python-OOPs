import os
import csv

file_path = os.path.join("util", "weather_data.csv")
current_dir = os.getcwd()
full_path = os.path.join(current_dir, file_path)

with open(full_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for temp in data:
        if temp[1] != "temp":
            temperatures.append(int(temp[1]))
