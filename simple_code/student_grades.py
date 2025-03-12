import pprint

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    grade = ''

    if 91 <= score <= 100:
        grade = 'Outstanding'
    elif 81 <= score <= 90:
        grade = 'Exceeds Expectations'
    elif 71 <= score <= 80:
        grade = 'Acceptable'
    else:
        grade = 'Fail'

    student_grades[key] = grade


pprint.pprint(student_scores)
pprint.pprint(student_grades)