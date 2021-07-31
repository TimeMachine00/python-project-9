print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to grade calculator")



student_scores = {
    "Munna": 81,
    "Bunny": 78,
    "Vasu": 99,
    "Paru": 74,
    "Latha": 62,
}



student_grades = {}


for i in student_scores:
    print(student_scores[i])
    if student_scores[i] > 90:
        student_grades[i] = 'outstanding'
    elif student_scores[i] < 90 and student_scores[i] > 70:
        student_grades[i] = 'exceed expectations'
    elif student_scores[i] < 70 and student_scores[i] > 60:
        student_grades[i] = 'good'
    elif student_scores[i] < 60 and student_scores[i] > 40:
        student_grades[i] = 'need improvement'

print(student_grades)
