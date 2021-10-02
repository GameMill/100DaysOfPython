import random


names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

students_scores = {student:random.randint(0,100) for student in names}
print(students_scores)

passed_students = {key:value for (key,value) in students_scores.items() if value >= 75}
print(passed_students)