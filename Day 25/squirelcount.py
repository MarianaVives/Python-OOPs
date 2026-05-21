import os
import csv
import pandas as pd

"""The information for this class is accessible in: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data"""

file_path = os.path.join("util", "squirrel_data.csv")
current_dir = os.getcwd()
full_path = os.path.join(current_dir, file_path)

data = pd.read_csv(full_path)

#Get all squirrel colors as a list
squirrel_color = data["Primary Fur Color"].tolist()

gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
red_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])

print(f"Red squirrel count: {red_sq}, Gray squirrel count: {gray_sq}, Black squirrel count: {black_sq}")

#Write these data as an object, save it in a data frame and create a csv file with the required information
data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count" : [red_sq, gray_sq, black_sq],
}

data_squirrels = pd.DataFrame(data_dict)
data_squirrels.to_csv("squirrels.csv")