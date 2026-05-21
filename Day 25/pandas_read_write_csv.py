import pandas as pd
import os

file_path = os.path.join("util", "weather_data.csv")
current_dir = os.getcwd()
full_path = os.path.join(current_dir, file_path)

data = pd.read_csv(full_path)
#print(type(data_temperature)) #dataFrame = spreadsheet/table
#print(type(data_temperature["temp"])) #series = a column

#convert data into a dictionary
data_dict = data.to_dict()
print(data_dict)

#convert to list
temperature_list = data["temp"].to_list()
print(temperature_list)
#Get mean
print(f"Average temperature ", str(sum(temperature_list)/len(temperature_list)))
print("average temperature using methods", str(data["temp"].mean()))
#Get max
print("Highest temperature ", str(data["temp"].max()))
#Get a row where day = Monday
print(data[data.day == "Monday"])
"""
"""
#Get the day where temperture is max
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)
#Get monday's temperature and convert to Celsius
def convert_to_farenheit(temperature):
    temperature = temperature * 1.8 + 32
    return round(temperature, 2)

print(convert_to_farenheit(monday.temp))

#Create a data frame from a dictionary
data_students = {
    "students":["amy", "bob","Mia"],
 "grades": [80,90,100]
}

data_frame_new = pd.DataFrame(data_students)
data_frame_new.to_csv("data_student_grades.csv")