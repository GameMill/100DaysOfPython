student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Daraco":74,
    "Neville":62
}

Student_grade = {}

for item in student_scores:
    if student_scores[item] >= 91:
        Student_grade[item] = "Oustanding"
    elif student_scores[item] >= 81:
        Student_grade[item] = "Exceeds Expectations"
    elif student_scores[item] >= 71:
        Student_grade[item] = "Acceptable"
    else:
        Student_grade[item] = "Fail"
    
print(Student_grade)