from numpy import fabs, nan
import pandas
import os 

root = os.path.dirname(os.path.abspath(__file__)) + "/"
data = pandas.read_csv(f"{root}2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = {"Fur Color":[],"Count":[]}


for item in data["Primary Fur Color"]:
    if(str(item) == "nan"):
        continue
    if(colors["Fur Color"].__contains__(item) == False):
        colors["Fur Color"].append(item)
        colors["Count"].append(1)
    else:
        colors["Count"][colors["Fur Color"].index(item)] += 1

colors = pandas.DataFrame(colors)
colors.to_csv(f"{root}squirrel_count.csv")
print(colors)
    
