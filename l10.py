student_names = [ "alice", "bob", "charlie"]
midterm1_grades = [90, 92, 78]
midterm2_grades = [92, 79, 95]
final_grades = [90, 85, 80]

def calc_letter_grade(student_names, midterm1, midterm2, final):
    final_letter_grades = []
    for i in range(len(student_names)):
        result = (midterm1[i]*0.3 + midterm2[i]*0.3 + final[i]*0.4)
        if result >= 90:
            final_letter_grades.append('A')
        elif result >= 85:
            final_letter_grades.append('B')
        elif result >= 80:
            final_letter_grades.append('C')
        elif result >= 75:
            final_letter_grades.append('D')
        else:
            final_letter_grades.append('F')
    return final_letter_grades

final_letter_grades = calc_letter_grade(student_names, midterm1_grades, midterm2_grades, final_grades)

print(final_letter_grades)