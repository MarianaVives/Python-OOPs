import random
import pandas
#Dictionary Comprehension - create a dictionary using a shorter syntax
#new_dict = {new_key: new_value for item in list}
#new_dict = {new_key: new_value for (key,value) in dict.items()}

names = ["luna", "lee", "lyn", "lucy", "leopolda", "lily", "lisa", "leonora"]

student_scores = {student:random.randint(0,10) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score>=6}
print(passed_students)

#Dictionary that counts the letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
l_sentence=sentence.split()
result = {l:len(l) for l in l_sentence}
print(result)


#Dictionary that converts C to F
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {d:(w * 9/5) + 32 for (d, w) in weather_c.items()}
print(weather_f)

#Dataframe

student_dic = {
    "Student": ["Lucy", "linda", "luna"],
    "Score": [10, 9, 9.5]
}
student_dataframe = pandas.DataFrame(student_dic)
print(student_dataframe)

#Loop through dictionary using dataframe
for (index, row) in student_dataframe.iterrows():
    #print(index)
    print(row.Student)
    if row.Student == "luna":
        print(row["Score"])