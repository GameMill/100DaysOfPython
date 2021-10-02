sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {key:len(key) for key in sentence.split(" ")}


print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {key:(temp_c * 9/5) + 32 for (key,temp_c) in weather_c.items()}


import pandas

print(weather_f)

student_dict = {
    "student": ["Angela","James","Lily"],
    "score":[56,76,98]
}
for (key,value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (key,value) in student_data_frame.items():
    print(key)

# loop through rows of a data frame

for(index,row) in student_data_frame.iterrows():
    print(row.student)