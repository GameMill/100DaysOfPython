import os
root = os.path.dirname(os.path.abspath(__file__)) + "/"


with open(f"{root}file1.txt") as file1:
    file1_data = [int(num.strip()) for num in file1.readlines()]
with open(f"{root}file2.txt") as file2:
    file2_data = [int(num.strip()) for num in file2.readlines()]
    
overlap_data = [num for num in file1_data if file2_data.__contains__(num)]
print(overlap_data)