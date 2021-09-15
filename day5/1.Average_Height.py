student_heights = [180,124,165,173,189,169,146]
arg_height = 0
for student_height in student_heights:
    arg_height += student_height

arg_height = round(arg_height/len(student_heights))
print(f"The Average student height is {arg_height:.0f}")