import os

root = os.path.dirname(os.path.abspath(__file__)) + "/"
data = {}
header_row = None
with open(f"{root}weather_data.csv") as csv_file:
    for row in csv_file:
        if(header_row == None):
            header_row = row.split(",")
            for header in header_row:
                data[header.strip()] = []
        else:
            value_row = row.split(",")
            for i in  range(len(header_row)):
                value = value_row[i].strip()
                try:
                    a = int(value)
                    value = a
                except:
                    pass
                data[header_row[i].strip()].insert(i,value)

temp = 0
i = 0
for item in data["temp"]:
    temp += item
    i += 1

print(f"Avg Temp = {temp/i:0.2f}c")