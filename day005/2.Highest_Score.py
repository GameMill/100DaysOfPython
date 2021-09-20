student_scores = [78,65,89,86,55,91,64,89]

height_score = 0
for student_score in student_scores:
    if student_score > height_score:
        height_score = student_score
        
print(f"The highest score in the class is: {height_score}")
        