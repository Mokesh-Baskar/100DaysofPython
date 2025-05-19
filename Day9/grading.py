#lets create a basic gradin program which grades teh students based ontheir mark
#scenario is simple where the sytem has thge dat of marks each student got as dictionry with key value pairs
#sytem must assess the marks and create a new dictionary with the grades baed on the mark and print the grrades one by one with student name

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}


for names in student_scores:
    if student_scores[names] >90 and student_scores[names] <= 100 :
        student_grades[names] = "Outstanding"
    elif student_scores[names] >80 and student_scores[names] <= 90 :
        student_grades[names] = "Exceeds Expectations"
    elif student_scores[names] >70 and student_scores[names] <= 80 :
        student_grades[names] = "Acceptable"
    else:
        student_grades[names] = "Fail"
        
for names in student_grades:

    print(f"Studnet {names} has got {student_grades[names]} grade")

    
            