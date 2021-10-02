import pandas
import os
root = os.path.dirname(os.path.abspath(__file__)) + "/"
data = pandas.read_csv(f"{root}weather_data.csv")

print(type(data))
print(type(data["temp"]))

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


print(data["temp"].max())

data = {
    "students": ["Amy","James","Angela"],
    "scores":[76,56,65]
}
data = pandas.DataFrame(data)
print(data)